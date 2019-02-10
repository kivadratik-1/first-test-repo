# our base image

FROM kivadratik/test:test-django-2.0.10

# specify the port number the container should expose
EXPOSE 8000/tcp


WORKDIR /home

# copy latest local files
COPY . .

VOLUME /home/db

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


