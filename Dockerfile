FROM python:3.10.4

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt .


RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver"]