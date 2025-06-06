import os

import sendgrid
from agents import function_tool
from dotenv import load_dotenv
from sendgrid import Email, To, Content, Mail

load_dotenv()


@function_tool
def send_email(subject: str, content: str):
    print(f"Sending email: {content}")
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(os.environ.get('SENDGRID_FROM_EMAIL'))
    to_email = To(os.environ.get('SENDGRID_TO_EMAIL'))
    content = Content("text/html", content)

    mail = Mail(from_email=from_email,
                to_emails=to_email,
                subject=subject,
                html_content=content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}
