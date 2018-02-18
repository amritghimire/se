# Generated by Django 2.0 on 2018-02-18 15:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
