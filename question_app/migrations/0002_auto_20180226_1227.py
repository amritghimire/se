# Generated by Django 2.0 on 2018-02-26 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0003_auto_20180223_1515'),
        ('product_app', '0002_auto_20180226_1227'),
        ('category_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(blank=True, to='category_app.Category'),
        ),
        migrations.AddField(
            model_name='question',
            name='downvoted_by',
            field=models.ManyToManyField(blank=True, related_name='downvoted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(blank=True, to='product_app.Product'),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(blank=True, to='tag.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
