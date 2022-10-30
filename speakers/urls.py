from django.urls import path
from speakers.views import show_speakers, show_speakers_info, SearchResultsView

app_name = 'speakers'

urlpatterns = [
    path('', show_speakers, name='show_speakers'),
    path('show_speakers_info/', show_speakers_info, name='show_speakers_info'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]