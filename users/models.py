from django.db import models
from django.utils import timezone


class Guest(models.Model):
    guestname = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    guest_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.save()

    def printout(self):
        pass

    def __str__(self):
        return self.username
