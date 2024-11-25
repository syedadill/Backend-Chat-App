#run these commands step by step in terminal

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


test the API's at
http://localhost:8000/api/register
http://localhost:8000/api/token
http://localhost:8000/api/token/refresh
