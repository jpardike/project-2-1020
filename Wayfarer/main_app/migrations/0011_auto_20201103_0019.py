# Generated by Django 3.1.2 on 2020-11-03 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20201102_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='images/profile_pics/place_holder.jpg', null=True, upload_to='images/profile_pics/'),
        ),
    ]