# Generated by Django 4.2.3 on 2023-07-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
                ('short_url', models.CharField(max_length=10000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]