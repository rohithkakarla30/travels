# Generated by Django 4.2.10 on 2024-02-12 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TripRecords", "0004_alter_user_packages_date_alter_user_packages_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_packages",
            name="date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
