from django.urls import path
from events.views import show_events_general, show_events_general23, show_events_general24, show_events_general25, show_json

app_name = 'events'

urlpatterns = [
    path('', show_events_general, name='show_events_general'),
    path('23/', show_events_general23, name='show_events_general23'),
    path('24/', show_events_general24, name='show_events_general24'),
    path('25/', show_events_general25, name='show_events_general25'),
    path('json/', show_json, name='show_json'),
]