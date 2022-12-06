from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='نام و نام خانوادگی'
    )
    username = models.CharField(
        max_length=50,
        verbose_name='نام کاربری',
        null=False,
        blank=False
    )
    password = models.CharField(
        max_length=50,
        verbose_name='گذرواژه',
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name='شماره موبایل',
        null=False,
        blank=False
    )


class Student(User):
    student_number = models.CharField(
        max_length=12,
        verbose_name='شماره دانشجویی',
        null=False,
        blank=False
    )
