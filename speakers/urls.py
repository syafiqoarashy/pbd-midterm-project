from django.urls import path
<<<<<<< HEAD
from speakers.views import show_speakers, search_speakers, show_speakers_info
=======
from speakers.views import show_speakers, show_speakers_info, SearchResultsView
>>>>>>> d0e944f (resolve conflict)

app_name = 'speakers'

urlpatterns = [
    path('', show_speakers, name='show_speakers'),
<<<<<<< HEAD
    path('search_speakers/', search_speakers.as_view(), name='search_speakers'),
    path('show_speakers_info/', show_speakers_info, name='show_speakers_info'),
    path("search/", search_speakers.as_view(), name="search_results"),
=======
    path('show_speakers_info/', show_speakers_info, name='show_speakers_info'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
>>>>>>> d0e944f (resolve conflict)
]