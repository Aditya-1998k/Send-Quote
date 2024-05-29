import os
from dotenv import load_dotenv
from mail import send_email
from letter_format import letter_body

load_dotenv()

from_email = os.getenv("EMAIL")
to_email = ["aditya98gupta@gmail.com", "gaditya@zeomega.com"]
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")

SUBJECT = "HAPPY WELL-BEING"

send_email(
    SUBJECT,
    letter_body(),
    from_email,
    to_email,
    smtp_server,
    smtp_port,
    smtp_username,
    smtp_password,
)
