# Generated by Django 4.0.1 on 2022-02-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=250)),
                ('allowed_user', models.CharField(max_length=250)),
            ],
        ),
    ]
