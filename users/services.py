import requests
from config import settings


class MyBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = settings.TELEGRAM_BOT_API_KEY

    def send_message_about_habit_time(self, text, recipient_chat_id=1453749466):
        """Отправка уведомления о привычке через Telegram"""
        requests.post(
            url=f"{self.URL}{self.TOKEN}/sendMessage",
            data={
                "chat_id": recipient_chat_id,
                "text": text
            }
        )
