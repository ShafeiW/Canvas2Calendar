from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime
from config import GOOGLE_CREDENTIALS_FILE, TIMEZONE

# Authenticate with Google Calendar API using Service Account
SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = service_account.Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=creds)

# Use the correct calendar ID
CALENDAR_ID = "shafei.waqar@gmail.com"  # Update with your actual Calendar ID

def event_exists(summary, due_date):
    """Check if an event already exists on Google Calendar."""
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        q=summary,  # Search by title
        timeMin=due_date,  # Check for future events
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    for event in events_result.get("items", []):
        if event["start"].get("dateTime") == due_date:
            print(f"⚠️ Event already exists: {summary}")
            return True

    return False

def add_event(summary, due_date):
    """Creates an event in Google Calendar if it does not already exist."""
    print(f"Adding event: {summary} at {due_date}")  # Debugging

    if event_exists(summary, due_date):
        print(f"⏭️ Skipping duplicate event: {summary}")
        return

    event = {
        "summary": summary,
        "start": {"dateTime": due_date, "timeZone": TIMEZONE},
        "end": {"dateTime": due_date, "timeZone": TIMEZONE},
    }

    try:
        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f"✅ Event created: {created_event.get('htmlLink')}")
    except Exception as e:
        print(f"❌ Error adding event: {e}")

if __name__ == "__main__":
    # Test adding a sample event
    test_date = "2025-02-15T23:59:00-08:00"  # Adjusted for PST timezone
    add_event("Test Assignment", test_date)
