from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('Userlogin', views.Userlogin, name='Userlogin'),
    path('Userlogout', views.Userlogout, name='Userlogout'),
    path('register', views.register, name='register'),
    path('invest', views.invest, name='invest'),
    path('ideas', views.ideas, name='ideas'),
    path('invest_idea/<int:Idea_id>/', views.invest_idea, name='invest_idea'),
]
