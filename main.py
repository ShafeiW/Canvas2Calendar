from datetime import datetime, timezone
import schedule
import time
from fetch_canvas import fetch_all_assignments
from add_to_calendar import add_event

def convert_canvas_date(canvas_date):
    """Converts Canvas API date to Google Calendar format (ISO 8601)."""
    return datetime.fromisoformat(canvas_date.replace("Z", "+00:00"))

def sync_assignments():
    """Fetches Canvas assignments and adds them to Google Calendar."""
    assignments = fetch_all_assignments()
    now = datetime.now(timezone.utc)  # Current time in UTC

    for assignment in assignments:
        event_title = f"{assignment['course']}: {assignment['name']}"
        event_date = convert_canvas_date(assignment["due_date"])

        # ✅ Skip past assignments
        if event_date < now:
            print(f"Skipping past assignment: {event_title} (Due: {event_date})")
            continue

        add_event(event_title, event_date.isoformat())
        print(f"Added: {event_title} on {event_date}")

# Schedule the script to run every 2 days
schedule.every(2).days.do(sync_assignments)

if __name__ == "__main__":
    print("📅 Canvas2Calendar is running every 2 days...")
    while True:
        schedule.run_pending()
        time.sleep(3600)  # Check every hour
