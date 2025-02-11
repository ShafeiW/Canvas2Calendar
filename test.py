from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
from config import GOOGLE_CREDENTIALS_FILE, TIMEZONE

SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = service_account.Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
service = build("calendar", "v3", credentials=creds)

now = datetime.utcnow().isoformat() + "Z"  # 'Z' means UTC time

events_result = service.events().list(
    calendarId="primary", timeMin=now, maxResults=10, singleEvents=True,
    orderBy="startTime").execute()

events = events_result.get("items", [])

if not events:
    print("No upcoming events found.")
else:
    print("Upcoming events:")
    for event in events:
        print(f"{event['summary']} - {event['start'].get('dateTime', event['start'].get('date'))}")
