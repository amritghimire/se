# Generated by Django 2.0 on 2018-02-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20180207_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='image/profile/'),
        ),
    ]