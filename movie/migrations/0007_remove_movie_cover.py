# Generated by Django 4.1.3 on 2022-11-15 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0006_remove_movie_pub_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="movie", name="cover",),
    ]