# Generated by Django 3.1.2 on 2020-11-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20201104_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
