from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('account_needed/', views.account_needed, name='account_needed'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('user/', views.user, name="user"),
    path('check_username/', views.check_username, name="check_username"),
]
