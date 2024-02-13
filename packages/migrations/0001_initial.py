# Generated by Django 4.2.10 on 2024-02-11 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amenities",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Packages",
            fields=[
                ("package_id", models.AutoField(primary_key=True, serialize=False)),
                ("package_name", models.CharField(max_length=255)),
                ("description", models.TextField(max_length=255)),
                ("duration_in_days", models.IntegerField()),
                (
                    "price_per_person",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("available_slots", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Places",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="places",
                        to="packages.packages",
                    ),
                ),
            ],
        ),
    ]
