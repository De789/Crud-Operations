from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_order_confirmation_email(order_id=user.email):
    subject="Order confimation"
    message=f"Your order with id {user_id} has been received and is being processed"
    return send_mail(sebject,message,settings.DEFAULT_FROM_EMAIL,[user.mail])