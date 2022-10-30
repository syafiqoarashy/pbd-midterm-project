from django.urls import path
from events.views import show_events_general

app_name = 'events'

urlpatterns = [
    path('', show_events_general, name='show_events_general'),
]