# Generated by Django 4.2.15 on 2024-08-25 03:01

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_face_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="face_image",
            field=models.ImageField(
                blank=True, null=True, upload_to=accounts.models.image_path, verbose_name="顔写真"
            ),
        ),
    ]
