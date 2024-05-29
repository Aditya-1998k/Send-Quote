"""Import all the third party module"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, from_email, to_emails,
               smtp_server, smtp_port, smtp_username,
               smtp_password):
    """Function to send mail"""

    msg = MIMEMultipart()
    msg['From'] = f"ADITYA GUPTA <{from_email}>"
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    for to_email in to_emails:
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
    server.quit()
