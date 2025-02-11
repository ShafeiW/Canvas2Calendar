from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import GOOGLE_CREDENTIALS_FILE

SCOPES = ["https://www.googleapis.com/auth/calendar"]
creds = service_account.Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
service = build("calendar", "v3", credentials=creds)

CALENDAR_ID = "shafei.waqar@gmail.com"  # Replace with your actual Google Calendar email

try:
    calendar = service.calendars().get(calendarId=CALENDAR_ID).execute()
    print(f"✅ Service account has access to: {calendar['summary']}")
except Exception as e:
    print(f"❌ Service account does NOT have access: {e}")
