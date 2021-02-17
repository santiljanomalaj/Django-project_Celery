web: gunicorn abanerd_django.wsgi
worker: celery --app abanerd  worker -l info
release: make migrateall