from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Post


@receiver(signal=post_save, sender=get_user_model())
def create_hello_post_signal(sender, instance, created, **kwargs):
    if created:
        p = Post(
            author=instance,
            title="First Post",
            content=f"Я {instance.username} и это мой первый пост тут!"
        )
        p.save()
