from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)




@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'A new post "{instance.title}" has been created by {instance.author}.'
        send_mail(subject, message, 'gdprasad520@gmail.com', [instance.author.email])

