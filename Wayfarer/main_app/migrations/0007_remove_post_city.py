# Generated by Django 3.1.2 on 2020-11-02 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_post_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
    ]
