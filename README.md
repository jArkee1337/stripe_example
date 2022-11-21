Выполнение тестового задания

Ссылка на тестовое: https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

Установка

Клонируем репозиторий на свою локальную машину

git clone https://github.com/jArkee1337/stripe_example.git

Создаем виртуальное окружение

python -m venv venv

source ./venv/bin/activate

Устанавливаем необходимые зависимости следующей командой

pip install -r requirements.txt

Cоздаем .env file со следующей структурой в корне проекта:

DEBUG=1

SECRET_KEY=yoursecretkey

DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]

SQL_ENGINE=django.db.backends.

SQL_DATABASE=stripe

SQL_USER=stripe_user

SQL_PASSWORD=stripe_user

SQL_HOST=db

SQL_PORT=5432

STRIPE_KEY=print here your secret stripe key without spaces


Настраиваем БД postgresql

Подключаемся к оболочке psql для этого в терминале выполним команду: sudo postgres psql

Создаем базу данных для проекта: CREATE DATABASE stripe;

Создаем пользователя с паролем для нашей БД: CREATE USER stripe_user WITH PASSWORD 'stripe_user';

Задайте кодировку стандарта UTF-8: ALTER ROLE stripe_user SET client_encoding TO 'utf8';

Задаем схему изоляцию транзакции: ALTER ROLE stripe_user SET default_transaction_isolation TO 'read committed';

Устанавливаем стандарт времени UTC: ALTER ROLE stripe_user SET timezone TO 'UTC';

Разрешаем пользователю доступ для управления БД: GRANT ALL PRIVILEGES ON DATABASE stripe TO stripe_user;

Закрываем консоль postgresql: \q

Создаем и выполняем миграции БД:

python manage.py makemigrations

python manage.py migrate

Запускаем приложение при помощи команды: docker-compose up --build

Выполняем миграции: docker-compose exec web python manage.py migrate --noinput

Создаем суперпользователя для доступа к django-admin: docker-compose exec web python manage.py createsuperuser



