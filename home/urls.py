from django.urls import path
from home.views import landing, login_user, register, landing_logged, show_data_json,create_testimonial


app_name = 'home'

urlpatterns = [
    path('', landing, name='landing'),
    path('logged/', landing_logged, name='landing_logged'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('json/', show_data_json, name='show_data_json'),
    path('add/', create_testimonial, name='add'),
]