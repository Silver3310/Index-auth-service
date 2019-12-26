import logging
import datetime
from smtplib import SMTPException

from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import EmailMessage

from celery import shared_task

User = get_user_model()

logger = logging.getLogger(__name__)


@shared_task
def send_email(
    title: str,
    body: str,
    email: str
) -> int:
    """Send an email to a user who has to approve or refuse a friendship"""
    email_msg = EmailMessage(
        title,
        body,
        settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    result = False
    try:
        result = email_msg.send()  # 1 if successful
    except SMTPException as e:
        logger.warning(
            "{datetime_now}: email for {email} failed with the message "
            "'{error}'".format(
                datetime_now=str(datetime.datetime.now()),
                email=email,
                error=e
            )
        )

    return True if result == 1 else False
