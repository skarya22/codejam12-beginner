# Generated by Django 4.1.3 on 2022-11-15 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0003_alter_movie_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="pub_date",
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
