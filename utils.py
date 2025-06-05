import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def generate_email_text(name, position, company, app_date):
    prompt = f"""
    Write a concise, polite follow-up email to {company} for a {position} application submitted by {name} on {app_date}. Be professional and clear.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def send_gmail_message(recipient, subject, body_text):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=58713)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        message = MIMEText(body_text)
        message["to"] = recipient
        message["from"] = "me"
        message["subject"] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        service.users().messages().send(userId="me", body={"raw": raw_message}).execute()
        return True
    except Exception as e:
        print("Error sending Gmail message:", e)
        return False
