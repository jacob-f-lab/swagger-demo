# Generated by Django 4.2.7 on 2023-11-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StickyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('created_user', models.EmailField(max_length=254)),
            ],
        ),
    ]
