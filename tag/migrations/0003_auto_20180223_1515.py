# Generated by Django 2.0 on 2018-02-23 15:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20180218_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='selected_by',
            field=models.ManyToManyField(blank=True, related_name='selected_tag', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='viewed',
            field=models.ManyToManyField(blank=True, related_name='viewed_tag', to=settings.AUTH_USER_MODEL),
        ),
    ]
