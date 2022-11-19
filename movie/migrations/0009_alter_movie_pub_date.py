# Generated by Django 4.1.3 on 2022-11-15 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0008_movie_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="pub_date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
