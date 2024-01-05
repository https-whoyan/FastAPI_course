import smtplib
from email.message import EmailMessage
from celeryconfing import CeleryConfig

from celery import Celery
from config import FASTAPI_MAILING_USER, FASTAPI_MAILING_KEY

celery_var = Celery('tasks', broker='redis://localhost:6379')
celery_var.config_from_object(CeleryConfig)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


# Email create
def get_email_template_dashboard(username: str, username_email: str):
    email = EmailMessage()
    email['Subject'] = "FastAPI Course Отчет"
    email['From'] = FASTAPI_MAILING_USER
    email['To'] = username_email
    email.set_content(
        f'<h1 style="color: red;">Здравствуйте, {username}, Шлю вам какой то отчет...</h1>'
    )
    return email


# Email send
@celery_var.task
def send_email_report_dashboard(username: str, username_email: str):
    email = get_email_template_dashboard(username, username_email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(FASTAPI_MAILING_USER, FASTAPI_MAILING_KEY)
        server.send_message(email)
