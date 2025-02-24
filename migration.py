import os

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.system("cls")
os.system("python manage.py runserver 8003")
