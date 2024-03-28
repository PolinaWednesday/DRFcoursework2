from django.core.management import BaseCommand
from habits.models import Habits
from users.services import MyBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_habits = Habits.objects.all()  # Получить все привычки из базы данных
        my_bot = MyBot()

        for habit in all_habits:
            my_bot.send_message_about_habit_time(
                f'Привет {habit.owner}! Время {habit.time}. '
                f'Пора идти в {habit.place} и сделать {habit.action}.'
                f'Это займет {habit.duration_time} минут!'
            )
