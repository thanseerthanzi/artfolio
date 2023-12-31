# Generated by Django 4.0.4 on 2023-10-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artist_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200)),
                ('pasword', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('ads', models.CharField(max_length=400)),
                ('district', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'artist_tbl',
            },
        ),
        migrations.CreateModel(
            name='guest_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'guest_tbl',
            },
        ),
    ]
