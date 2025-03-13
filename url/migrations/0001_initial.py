# Generated by Django 5.1.7 on 2025-03-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=10, unique=True)),
                ('url', models.URLField()),
                ('visits', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
