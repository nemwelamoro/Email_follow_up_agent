from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from dotenv import load_dotenv
import os

from utils import generate_email_text, send_gmail_message

# Load environment variables (e.g., Gmail + Gemini keys)
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Hardcoded follow-up email logic
def generate_and_send_email():
    recipient = "bendonmurgor@gmail.com"
    name = "John Doe"
    position = "Data Analyst"
    company = "Acme Inc"
    applied_at = "2025-05-10"

    subject = f"Follow-up on {position} Application at {company}"
    body = generate_email_text(name, position, company, applied_at)

    success = send_gmail_message(recipient, subject, body)
    if success:
        print("Follow-up sent.")
    else:
        print("Failed to send follow-up.")

#  Scheduler job that runs daily
def scheduled_followup_job():
    print("Running scheduled follow-up...")
    generate_and_send_email()

#  Configure and start APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_followup_job, trigger='interval', seconds=60)  # every 60 seconds
# Start it only once — avoid running in Flask reloader process
if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    scheduler.start()

# Flask route
@app.route("/")
def index():
    return "<h2>Email Follow-Up Agent is running. Scheduler is active.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
