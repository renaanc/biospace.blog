web: gunicorn biospace_site.wsgi:application
web: gunicorn biospace_site.wsgi:application --preload && python manage.py collectstatic --noinput
web: gunicorn biospace_site.wsgi:application --log-level=debug --access-logfile - --error-logfile -
