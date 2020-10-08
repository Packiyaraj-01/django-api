# Generated by Django 3.1.2 on 2020-10-08 07:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('capital', models.CharField(max_length=200)),
                ('citizenship', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
                ('currency_code', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tab_countries',
            },
        ),
    ]
