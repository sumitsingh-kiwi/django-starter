"""
mails file
"""
import logging
import os
from smtplib import SMTPException

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from apps.utility.constants import EMAIL_CONTENT

logger = logging.getLogger('__name__')


@shared_task()
def send_email(mail_type, data, frontend_url=None):
    """
`   used to send mail from everywhere in the project
    :param mail_type: type of the mail being sent
    :param data: extra data {'token': 'sdafafaf23dfgdfgds'}
    :param frontend_url: https://frontend.com
    :return:
    """
    if not frontend_url:
        data.update({'frontend_url': os.getenv('FRONT_END_URL')})
    else:
        data.update({'frontend_url': frontend_url})

    email_content = EMAIL_CONTENT[mail_type]
    subject = email_content['subject']

    html_message = render_to_string(
        email_content['template_name'], data)

    email_host = settings.FROM_EMAIL
    try:
        send_mail(subject, data.get('message', ""), email_host, [data['to_user']], html_message=html_message)
        return True
    except SMTPException as e:
        logger.exception("Sending Mail Exception : {}".format(str(e)))
        return False
