from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import CustomUserEditForm
from users.models import Lesson, Day, WeeklySchedule
from django.shortcuts import render, get_object_or_404, redirect
from users.forms import LessonForm
from django.shortcuts import render, redirect
from users.forms import CustomUserChangeForm


# Create your views here.
def index(request):
    return render(request, 'Djangoapp/index.html')


def about(request):
    return render(request, 'Djangoapp/explorer_base.html')


def news(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'Djangoapp/news.html', {'news_object': news})


def contacts(request):
    return render(request, 'Djangoapp/schedule.html')


def nachal(request):
    return render(request, 'Djangoapp/nachal.html', {'news': news})


def registr(request):
    return render(request, 'Djangoapp/registr.html')


def chats(request):
    return render(request, 'Djangoapp/chats-teacher.html')


def info(request):
    return render(request, 'Djangoapp/info.html')


def profile(request):
    return render(request, 'Djangoapp/profile.html')


def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('profile')
    else:
        form = CustomUserEditForm(instance=request.user)

    return render(request, 'Djangoapp/profile_edit.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Используем email для входа
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                if user.user_type == CustomUser.STUDENT:
                    return redirect('nachal')
                elif user.user_type == CustomUser.TEACHER:
                    return redirect('about')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def profile_view(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    context = {'user': user}
    return render(request, 'users/signup.html', context)


def profile(request):
    user = request.user
    form = CustomUserEditForm(instance=user)
    return render(request, 'Djangoapp/profile.html', {'user': user, 'form': form})


def lesson_list(request):
    days = Day.objects.all()
    times = Lesson.objects.values_list('time', flat=True).distinct().order_by('time')

    lessons_by_day = {}

    for day in days:
        weekly_schedule = WeeklySchedule.objects.filter(week_day=day).first()
        lessons_by_day[day] = weekly_schedule.lessons.all() if weekly_schedule else []

    table_data = []

    for time in times:
        row = {'time': time, 'lessons': []}
        for day in days:
            weekly_schedule = WeeklySchedule.objects.filter(week_day=day).first()
            lessons = weekly_schedule.lessons.filter(time=time) if weekly_schedule else []
            row['lessons'].append({'day': day, 'lessons': lessons})
        table_data.append(row)

    context = {
        'days': days,
        'times': times,
        'table_data': table_data,
    }

    return render(request, 'schedule/lesson_list.html', context)


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'schedule/lesson_detail.html', {'lesson': lesson})


def lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm()
    return render(request, 'schedule/lesson_edit.html', {'form': form})


def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'schedule/lesson_edit.html', {'form': form})


def profile_edition(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'Djangoapp/profile_edit.html', {'form': form})


def your_view(request):
    form = CustomUserChangeForm(initial={'birthdate': request.user.birthday})

    return render(request, 'profile_edit.html', {'form': form})
