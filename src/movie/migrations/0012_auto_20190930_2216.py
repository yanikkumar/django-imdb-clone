# Generated by Django 2.2.5 on 2019-09-30 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 16, 46, 18, 255609, tzinfo=utc)),
        ),
    ]