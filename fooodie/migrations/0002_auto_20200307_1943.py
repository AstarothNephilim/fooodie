# Generated by Django 2.2.3 on 2020-03-07 18:43

from django.db import migrations, models
import fooodie.models


class Migration(migrations.Migration):

    dependencies = [
        ('fooodie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=fooodie.models.user_directory_path),
        ),
    ]
