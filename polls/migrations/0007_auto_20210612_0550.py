# Generated by Django 3.2.4 on 2021-06-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210612_0431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='numberssssq',
        ),
        migrations.DeleteModel(
            name='phone_sms',
        ),
        migrations.AddField(
            model_name='company',
            name='rubsq',
            field=models.CharField(default='def', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='usasq',
            field=models.CharField(default='def', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='photo_company',
            field=models.ImageField(upload_to='photo'),
        ),
    ]
