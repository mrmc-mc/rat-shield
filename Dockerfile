FROM python:3.9-alpine
RUN mkdir -p /home/app
RUN mkdir -p /home/db
RUN pip install --upgrade pip 
COPY ./requirements.txt /home/app
RUN pip install -r /home/app/requirements.txt
COPY . /home/app
COPY ./db.sqlite3 /home/db/db.sqlite3
WORKDIR /home/app

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]