# Generated by Django 4.1.5 on 2023-01-17 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='موضوع')),
                ('suggestion_text', models.TextField(verbose_name='متن پیشنهاد')),
                ('submission_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت پیشنهاد')),
                ('related_department', models.CharField(max_length=200, verbose_name='بخش مربوطه')),
                ('state', models.CharField(choices=[('NOT CHECKED', 'بررسی نشده'), ('CHECKING', 'در حال بررسی'), ('CHECKED', 'بررسی شده')], max_length=50, verbose_name='وضعیت')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='cands.student', verbose_name='دانشجوی ثبت کننده پیشنهاد')),
            ],
        ),
    ]