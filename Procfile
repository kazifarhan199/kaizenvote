worker: sh -c 'python manage.py migrate'
web: gunicorn VootingWebsite.wsgi:application --log-file -
heroku ps:scale web=1