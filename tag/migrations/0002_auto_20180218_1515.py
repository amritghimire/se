# Generated by Django 2.0 on 2018-02-18 15:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='selected_by',
            field=models.ManyToManyField(related_name='selected_tag', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='viewed',
            field=models.ManyToManyField(related_name='viewed_tag', to=settings.AUTH_USER_MODEL),
        ),
    ]