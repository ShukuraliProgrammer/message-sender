import json
from datetime import datetime

from django.db.models.signals import post_save
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from .models import Message, UserModel


def post_save_wishlist_date(sender, instance: Message, created, **kwargs):
    if created:
        user = instance.user
        clocked_schedule = ClockedSchedule.objects.create(clocked_time=user.birth_day)
        PeriodicTask.objects.create(
            name=f"Message is sending to Telegram Bot: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            clocked=clocked_schedule,
            task="msg_app.tasks.send_message_for_notify",
            enabled=True,
            one_off=True,
            kwargs=json.dumps({"telegram_id": str(user.telegram_id), "message": str(instance.text)}),
        )


post_save.connect(post_save_wishlist_date, sender=Message)
