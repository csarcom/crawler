# Generated by Django 2.0.4 on 2018-04-30 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_url',
            field=models.URLField(unique=True, verbose_name='post_url'),
        ),
    ]
