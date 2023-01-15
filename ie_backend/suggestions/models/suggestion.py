from django.db import models

from suggestions.enums import SUGGESTION_STATES
from suggestions.models import Student


class Suggestion(models.Model):
    subject = models.CharField(
        max_length=250,
        verbose_name='موضوع'
    )
    suggestion_text = models.TextField(
        verbose_name='متن پیشنهاد'
    )
    submission_date = models.DateTimeField(
        verbose_name='تاریخ ثبت پیشنهاد',
        auto_now=True,
    )
    related_department = models.CharField(
        max_length=200,
        verbose_name='بخش مربوطه'
    )
    student = models.ForeignKey(
        to=Student,
        related_name='suggestions',
        on_delete=models.CASCADE,
        verbose_name='دانشجوی ثبت کننده پیشنهاد'
    )
    state = models.CharField(
        max_length=50,
        choices=SUGGESTION_STATES,
        verbose_name='وضعیت'
    )

    def __str__(self):
        return "{} - {}".format(self.subject, self.submission_date.date())

