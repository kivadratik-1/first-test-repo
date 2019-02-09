# our base image
#FROM sha256:07eaeb9e87f1640d341eaca076336eeded7ab4a9a1478faf216c4ce481a1810e

FROM kivadratik/test:test-django-2.0.10

# specify the port number the container should expose
EXPOSE 8000/tcp


WORKDIR /home

# copy latest local files
COPY . .

VOLUME /home/db

# run the application
# CMD ["python3", "./test-mqtt-sender.py"]
#CMD []
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python3", "manage.py", "makemigrations"]
CMD ["python3", "manage.py", "migrate"]

