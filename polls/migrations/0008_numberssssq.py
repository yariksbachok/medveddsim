# Generated by Django 3.2.4 on 2021-06-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210612_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='numberssssq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(choices=[('KNK', 'Канада'), ('USA', 'США'), ('RUS', 'Россия'), ('NDN', 'Нидерланды'), ('FRF', 'Франция'), ('ISI', 'Испания'), ('ITI', 'Италия'), ('AVA', 'Австрия'), ('UKU', 'Англия'), ('GER', 'Германия')], default='USA', max_length=5)),
                ('shirt_company', models.CharField(choices=[], default='App', max_length=15)),
                ('price_rubsq', models.CharField(max_length=100)),
                ('price_usasq', models.CharField(max_length=100)),
                ('number_phonesq', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номер',
            },
        ),
    ]
