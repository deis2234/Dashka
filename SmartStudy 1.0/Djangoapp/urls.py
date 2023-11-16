from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from users.views import SignUpView, LoginUser
from .views import lesson_list, lesson_detail, lesson_new, lesson_edit

urlpatterns = [
    path('', LoginUser.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('nachal', views.nachal, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('chats', views.chats, name='chats'),
    path('info', views.info, name='info'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile-edit'),
    path('news/<int:news_id>/', views.news, name='news'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lessons/', lesson_list, name='lesson_list'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('lesson/new/', lesson_new, name='lesson_new'),
    path('lesson/<int:pk>/edit/', lesson_edit, name='lesson_edit'),
]
