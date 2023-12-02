from users.models import Lesson, Day


class DaySchedule:
    def __init__(self, day: Day):
        self.day = day
        self.lessons = list(Lesson.objects.filter(day=day.pk).order_by('time'))


class WeekSchedule:
    def __init__(self):
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        self.days = sorted(list(Day.objects.all()), key=lambda x: days_of_week.index(x.name))
        self.schedule = [DaySchedule(day) for day in self.days]
