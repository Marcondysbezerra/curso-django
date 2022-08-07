# Generated by Django 4.0.6 on 2022-08-01 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('vimeo_id', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
