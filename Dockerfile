# our base image
FROM sha256:2cac85eb6545f29f1c5e61e0d7f00b862bc5db869d2367eba2d5c7482f838dc2

# specify the port number the container should expose
EXPOSE 8000/tcp


WORKDIR /home

# copy latest local files
COPY . .


# run the application
# CMD ["python3", "./test-mqtt-sender.py"]
#CMD []
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
