# Generated by Django 3.2 on 2021-06-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20210614_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numbers_of_phone',
            name='sms_kod',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
