from django.contrib.auth.models import User
from django.db import models


class AppUser(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='نام و نام خانوادگی'
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name='شماره موبایل',
        null=False,
        blank=False
    )


class Student(AppUser):
    student_number = models.CharField(
        max_length=12,
        verbose_name='شماره دانشجویی',
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return "{} - {}".format(self.student_number, self.name)

