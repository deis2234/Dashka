from django.urls import path
from . import views
from users.views import SignUpView, LoginUser

urlpatterns = [
    path('', LoginUser.as_view() ,name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('nachal', views.nachal, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('chats', views.chats, name='chats'),
    path('info', views.info, name='info'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile-edit'),
    path('news/<int:news_id>/', views.news, name='news')
]
