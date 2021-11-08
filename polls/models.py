from django.db import models


class company(models.Model):
    name_company = models.CharField(max_length=100)
    rubsq = models.CharField(max_length=100, default='def')
    usasq = models.CharField(max_length=100, default='def')
    photo_company = models.ImageField(upload_to='photo')
    def __str__(self):
        return self.name_company

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class numberssssq(models.Model):
    SHIRT_SIZES = (('KNK','Канада'),
                   ('USA', 'США'),
                   ('RUS','Россия'),
                   ('NDN', 'Нидерланды'),
                   ('FRF','Франция'),
                   ('ISI','Испания'),
                   ('ITI', 'Италия'),
                   ('AVA', 'Австрия'),
                   ('UKU', 'Англия'),
                   ('GER', 'Германия'))
    limit_choice = (('Отключен', 'Отключен'),
                    ('1 день', '1 день'),
                    ('3 дня', '3 дня'),
                    ('1 неделя', '1 неделя'),
                    ('2 недели', '2 недели'),
                    ('1 месяц', '1 месяц'),
                    ('2 месяца', '2 месяца'))
    shirt_size = models.CharField(max_length=5, choices=SHIRT_SIZES, default='USA')
    shirt_company = models.ForeignKey(company,  on_delete=models.CASCADE, blank=True, null=True)
    shirt_limit = models.CharField(max_length=15, choices=limit_choice, default='Отключен')
    number_phonesq = models.CharField(max_length=100)
    bool_number = models.BooleanField(default=True)
    def __str__(self):
        return self.number_phonesq
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номер'


class phone_sms(models.Model):
    phone = models.CharField(max_length=100)
    sms = models.CharField(max_length=100)

    def __str__(self):
        return self.sms

    class Meta:
        verbose_name = 'Смс'
        verbose_name_plural = 'Смс'



class numbers_of_phone(models.Model):
    id_user = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sms_kod = models.CharField(max_length=100, default=0)
    company = models.CharField(max_length=100)
    price_number = models.CharField(max_length=100)

    def __str__(self):
        return self.phone

class number_all(models.Model):
    SHIRT_SIZES = (('KNK', 'Канада'),
                   ('USA', 'США'),
                   ('RUS', 'Россия'),
                   ('NDN', 'Нидерланды'),
                   ('FRF', 'Франция'),
                   ('ISI', 'Испания'),
                   ('ITI', 'Италия'),
                   ('AVA', 'Австрия'),
                   ('UKU', 'Англия'),
                   ('GER', 'Германия'))

    HOURS_SIZES = (('none', 'none'),
                   ('one', 'one'),
                   ('two', 'two'),
                   ('three', 'three'),
                   ('four', 'four'),
                   ('five', 'five'))

    DAYS_SIZES = (('none', 'none'),
                   ('one', 'one'),
                   ('two', 'two'),
                   ('three', 'three'),
                   ('four', 'four'))
    WEEKS_SIZES = (('none', 'none'),
                  ('one', 'one'),
                  ('two', 'two'),
                  ('three', 'three'))

    MONSDAYS_SIZES = (('none', 'none'),
                     ('one', 'one'),
                     ('two', 'two'))

    shirt_sizes = models.CharField(max_length=5, choices=SHIRT_SIZES, default='USA')
    hours_sizes = models.CharField(max_length=5, choices=HOURS_SIZES, default='none')
    days_sizes = models.CharField(max_length=5, choices=DAYS_SIZES, default='none')
    weeks_sizes = models.CharField(max_length=5, choices=WEEKS_SIZES, default='none')
    monsday_sizes = models.CharField(max_length=5, choices=MONSDAYS_SIZES, default='none')
    shirt_company = models.ForeignKey(company, on_delete=models.CASCADE, blank=True, null=True)
    price_select = models.CharField(max_length=10000000, default='0')
    number_phone= models.CharField(max_length=100)
    bool_number = models.BooleanField(default=True)
    def __str__(self):
        return self.number_phone
    class Meta:
        verbose_name = 'Все номера'
        verbose_name_plural = 'Все номера'


