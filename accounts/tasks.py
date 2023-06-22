from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_login_email(user_email):
    subject = 'Welcome to Your Website'
    message = 'Your email message goes here'
    from_email = 'your-email@gmail.com'
    to_email = [user_email]
    send_mail(subject, message, from_email, to_email)
