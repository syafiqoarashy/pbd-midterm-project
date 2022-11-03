from django.urls import path
from speakers.views import show_speakers, search_speakers, show_speakers_info

app_name = 'speakers'

urlpatterns = [
    path('', show_speakers, name='show_speakers'),
    path('search_speakers/', search_speakers.as_view(), name='search_speakers'),
    path('show_speakers_info/', show_speakers_info, name='show_speakers_info'),
    path("search/", search_speakers.as_view(), name="search_results"),
]