from django.urls import path
from home.views import landing, login_user, register


app_name = 'home'

urlpatterns = [
    path('', landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
]