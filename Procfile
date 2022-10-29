release: sh -c 'python manage.py migrate && python manage.py loaddata submission_data.json && python manage.py loaddata track_data.json'
web: gunicorn project_django.wsgi --log-file -