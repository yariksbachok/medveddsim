# Generated by Django 3.2 on 2021-06-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_alter_numberssssq_shirt_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name_company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
