from django.contrib.auth.models import User
from django.db import models


class CandsUser(User):
    name = models.CharField(
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )


class Student(CandsUser):
    student_number = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{} - {}".format(self.student_number, self.name)
