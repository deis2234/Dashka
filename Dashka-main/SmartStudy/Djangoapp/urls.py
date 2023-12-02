from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from users.views import SignUpView, LoginUser
from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('nachal', lecture_list, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('chats', views.chats, name='chats'),
    path('info', views.info, name='info'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edition, name='profile-edit'),
    path('news/<int:news_id>/', views.news, name='news'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lessons/', lesson_list_alternative, name='lesson_list'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('lesson/new/', lesson_new, name='lesson_new'),
    path('lesson/<int:pk>/edit/', lesson_edit, name='lesson_edit'),
    path('nachal', lecture_list, name='lecture_list'),
    path('load_subfolders/<int:folder_id>/', views.load_subfolders, name='load_subfolders'),
    path('load_subfolders', load_subfolders, name='load_subfolders'),
    path('pi032', views.pi032, name='pi032'),
    path('pi022', views.pi022, name='pi022'),
    path('pi021', views.pi012, name='pi012'),
]
