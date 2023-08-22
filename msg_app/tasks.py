from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task


@shared_task(name="send_message_for_notify")
def send_message_for_notify(telegram_id, message):
    token = "5793056122:AAGTQV-B6-Hm0kQUYwY9QKzPABmVU5Nw0DM"
    api_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={telegram_id}&text={message}"
    response = requests.post(api_url)
    print(response.status_code)
