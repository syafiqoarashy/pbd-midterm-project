from django.urls import path
from .views import show_sessions, category, AME, BBE, CPE, ECE, IE, ISBE, IT, MME, SBCC, SCE, show_json_category

app_name = 'parallel_sessions'

urlpatterns = [
    path('', category, name='category'),
    path('category_sessions', show_sessions, name='category_sessions'),
    path('AME', AME, name="AME"),
    path('BBE', BBE, name="BBE"),
    path('CPE', CPE, name="CPE"),
    path('ECE', ECE, name="ECE"),
    path('IE', IE, name="IE"),
    path('ISBE', ISBE, name="ISBE"),
    path('IT', IT, name="IT"),
    path('MME', MME, name="MME"),
    path('SBCC', SBCC, name="SBCC"),
    path('SCE', SCE, name="SCE"),
    path('json_category/', show_json_category, name="json_category"),
    
]