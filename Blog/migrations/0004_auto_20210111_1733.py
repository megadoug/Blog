# Generated by Django 3.1.5 on 2021-01-11 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210111_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conteudos',
            new_name='conteudo',
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 20, 33, 32, 802611, tzinfo=utc)),
        ),
    ]
