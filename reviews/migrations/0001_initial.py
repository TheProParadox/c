# Generated by Django 3.2rc1 on 2021-07-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(default='', max_length=50)),
                ('movie_desc', models.CharField(default='', max_length=500)),
                ('image', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
