import requests
import json
from config import CANVAS_API_URL, CANVAS_ACCESS_TOKEN

def get_courses():
    """Fetches the list of enrolled courses from Canvas."""
    url = f"{CANVAS_API_URL}courses"
    headers = {"Authorization": f"Bearer {CANVAS_ACCESS_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        courses = response.json()
        print("Courses API Response:", json.dumps(courses, indent=2))  # Debug print
        return courses
    else:
        print(f"Error fetching courses: {response.status_code}, {response.text}")
        return []


def get_assignments(course_id):
    """Fetches assignments for a given course ID."""
    url = f"{CANVAS_API_URL}courses/{course_id}/assignments"
    headers = {"Authorization": f"Bearer {CANVAS_ACCESS_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching assignments for course {course_id}: {response.status_code}")
        return []

def fetch_all_assignments():
    """Fetches assignments for all enrolled courses."""
    courses = get_courses()
    all_assignments = []

    for course in courses:
        course_id = course.get("id")
        course_name = course.get("name", f"Course {course_id}")

        if not course_id:
            print(f"Skipping course due to missing ID: {course}")
            continue

        assignments = get_assignments(course_id)

        if isinstance(assignments, dict) and "errors" in assignments:
            print(f"Skipping course {course_name} due to access restrictions.")
            continue  # Skip courses with permission errors

        for assignment in assignments:
            if assignment.get("due_at"):
                all_assignments.append({
                    "course": course_name,
                    "name": assignment.get("name", "Unnamed Assignment"),
                    "due_date": assignment["due_at"]
                })

    return all_assignments



if __name__ == "__main__":
    assignments = fetch_all_assignments()
    print(json.dumps(assignments, indent=2))
