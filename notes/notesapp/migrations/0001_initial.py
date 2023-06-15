# Generated by Django 4.1.2 on 2023-06-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="note_model",
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
                ("text", models.TextField()),
                ("audio", models.FileField(blank=True, null=True, upload_to="audio/")),
                ("video", models.FileField(blank=True, null=True, upload_to="video/")),
            ],
        ),
    ]
