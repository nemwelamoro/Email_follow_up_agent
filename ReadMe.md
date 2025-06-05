# 📧 Email Follow-Up Agent

A lightweight Flask app that sends automated follow-up emails using the Gmail API and Gemini LLM. It's designed for job application platforms to help candidates stay engaged with employers.

---

## 🔧 Features

- **🧠 Email templating using Gemini LLM**: Generate personalized and contextually relevant email content.
- **📅 Automated scheduling via APScheduler**: Schedule follow-up emails to be sent automatically at predefined intervals.
- **🔐 Secure Gmail API integration with OAuth2**: Safely connect to your Gmail account for sending emails.
- **🌐 Flask web app with a running status page**: A simple web interface to monitor the application's status.
- **📦 Easy environment setup with `.env`**: Quickly configure necessary API keys and secrets.

---

## 🗂️ Project Structure

email_followup_agent/
├── app.py # Main Flask app and scheduler
├── utils.py # Functions: email generation + sending
├── credentials.json # Gmail OAuth2 credentials (private)
├── token.json # Generated Gmail access token
├── .env # Secret keys & API keys
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── templates/
└── index.html # Optional web UI

yaml
Copy code

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/email-followup-agent.git
cd email_followup_agent
bash
2. Create & Activate a Virtual Environment

Copy code
python -m venv env
On Windows:

bash
Copy code
env\Scripts\activate
On Mac/Linux:

bash
Copy code
source env/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up Gmail API
Visit Google Cloud Console.

Create a new project.

Enable the Gmail API.

Configure the OAuth Consent Screen.

Create an OAuth 2.0 Client ID (Type: Desktop).

Download credentials.json and place it in the project root directory.

5. Create .env File
Create a file named .env in the project root and add your secret keys:

env
Copy code
FLASK_SECRET_KEY=your_flask_secret_key
GEMINI_API_KEY=your_gemini_api_key
⚠️ Do not commit .env, credentials.json, or token.json to version control.

▶️ Running the App
bash
Copy code
python app.py
Visit the app in your browser: http://127.0.0.1:5000

Console output example:

csharp
Copy code
* Running on http://127.0.0.1:5000
Running scheduled follow-up...
Follow-up sent.
📨 Sample Email
Subject:

csharp
Copy code
Follow-up on Data Analyst Application at Acme Inc
Body:

css
Copy code
Hi John Doe,

I wanted to follow up on my application for the Data Analyst position at Acme Inc submitted on 2025-05-10.

Looking forward to hearing from you.

Best regards,  
John Doe
🔁 APScheduler Setup
For testing (runs every 60 seconds):

python
Copy code
scheduler.add_job(scheduled_followup_job, trigger='interval', seconds=60)
For production (daily at 9:00 AM):

python
Copy code
scheduler.add_job(scheduled_followup_job, trigger='cron', hour=9, minute=0)
vbnet
Copy code
