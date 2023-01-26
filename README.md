# The cake shop

## info
testing django

## how to
1. don't forget to add .env file with SECRET_KEY 
2. pip install -r requirements.txt
3. python manage.py runserver 0.0.0.0:8000
4. docker compose up -d
5. cd ./homework_09/shop$ celery -A shop worker -l INFO

## main goal
1. add rabbitmq and celery
2. add reg, login, logout functionality
3. set up user rights (ingredients cans see only staff, crud only staff)
4. выполнить тестирование своего приложения:
использовать setUp, tearDown;
проверять контекст.



