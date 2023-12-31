# Generated by Django 4.2.2 on 2023-10-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.DeleteModel(
            name='guest_tbl',
        ),
        migrations.RemoveField(
            model_name='artist_tbl',
            name='pasword',
        ),
        migrations.AddField(
            model_name='artist_tbl',
            name='photo',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
