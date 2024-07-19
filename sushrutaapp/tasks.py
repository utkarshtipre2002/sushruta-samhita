# celery / django imports
# from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import shared_task

# custom imports
from .email import send_review_email

logger = get_task_logger(__name__)


# @task(name="send_review_email_task")
@shared_task
def send_review_email_task(username, email, data):
    logger.info("Sent email")
    return send_review_email(username, email, data)
