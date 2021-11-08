from django.forms import model_to_dict
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.sites.models import Site
import re
from .models import *
import simplejson as json
from django.http.response import HttpResponse

def index(requests):
    if requests.user.is_active:
        item = []
        number = {}
        country ='USA'
        limit = 'Отключен'
        username = requests.user.username
        coun = numberssssq.objects.all()
        for i in coun:
            if i.shirt_size == country:
                items = company.objects.all()
                for j in items:
                    if limit == 'Отключен':
                        if str(j.name_company) == str(i.shirt_company) and j not in item:
                            n = numberssssq.objects.filter(shirt_size=country, shirt_company=j.id).count()
                            item.append(j)
                            number.setdefault(j.name_company, str(n))
                    elif j.name_company == i.shirt_company and i.shirt_limit == limit and j not in item:
                        n = numberssssq.objects.filter(shirt_size= country, shirt_company= j.name_company).count()
                        item.append(j)
                        number.setdefault(j.name_company, str(n))
        register_yes = 'yes'
        url = 'chek_number?'
        return render(requests, 'index.html', {'username':username, 'reqister':register_yes, 'url':url})
    else:
        url = 'chek_number?'
        return render(requests, 'index.html', {'url':url})


def free_number(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'free_number.html', {'username':username, 'reqister':register_yes, 'url':url})
    else:
        url = 'chek_number?'
        return render(requests, 'free_number.html', {'url':url})


def rent_time(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'rent_time.html', {'username':username, 'reqister':register_yes, 'url':url})
    else:
        url = 'chek_number?'
        return render(requests, 'rent_time.html', {'url':url})

def faq(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'FAQ.html', {'username':username, 'url':url, 'reqister':register_yes})
    else:
        url = 'chek_number?'
        return render(requests, 'FAQ.html', {'url':url})

def rent_active(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        ur = 'show_number?'
        return render(requests, 'rent_active.html', {'username':username, 'url':url, 'reqister':register_yes, 'ur':ur})
    else:
        url = 'chek_number?'
        return render(requests, 'rent_active.html', {'url':url})

def active_number(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        number = numbers_of_phone.objects.filter(id_user=requests.user.id).all()
        return render(requests, 'rent_number.html', {'username':username, 'phone_num':number, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'entrance.html')


def my_number(requests):
    if requests.user.is_active:
        number = numbers_of_phone.objects.filter(id_user=requests.user.id).all()
        number = [model_to_dict(num) for num in number]
        return HttpResponse(json.dumps(number))
    else:
        return render(requests, 'entrance.html')

def my_profile(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'my_profile.html', {'username':username, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'entrance.html')

@csrf_exempt
def change_password(requests):
    if requests.method == 'POST':
        user = auth.authenticate(username=requests.POST['name'], password=requests.POST['psw'])
        if user is not None:
            if user.is_active:
                user.set_password(requests.POST['rtpsw'])
                username = user.username
                user.save()
                url = 'chek_number?'
                register_yes = 'yes'
                return render(requests, 'my_profile.html', {'username': username, 'url':url, 'reqister':register_yes})
        else:
            eror = 'Вы сделали что-то не так'
            return render(requests, 'my_profile.html', {'eror_user': eror})

    elif requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'change_password.html', {'username': username, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'change_password.html')

@csrf_exempt
def exit(requests):
    if requests.method == 'POST':
        user = auth.authenticate(username=requests.POST['name'], password=requests.POST['psw'])
        if user is not None:
            if user.is_active:
                login(requests, user)
                username = user.username
                url = 'chek_number?'
                register_yes = 'yes'
                return render(requests, 'my_profile.html', {'username': username, 'url':url, 'reqister':register_yes})
        else:
            eror = 'Вы сделали что-то не так'
            return render(requests, 'entrance.html', {'eror_user': eror})
    else:
        logout(requests)
        return render(requests, 'entrance.html')

@csrf_exempt
def reg_auth(requests):
    if requests.method == 'POST':
        if requests.POST.get('psw') != requests.POST.get('retpsw'):
            eror = 'Пароли не совпадают'
            return render(requests, 'req_auth.html', {'eror_user': eror})

        elif User.objects.filter(username=requests.POST['name']).exists():
            eror = 'Вы сделали что-то не так'
            return render(requests, 'req_auth.html', {'eror_user': eror})

        else:
            user = User.objects.create_user(username=requests.POST['name'], password=requests.POST['psw'])
            login(requests, user)
            return render(requests, 'my_profile.html')
    return render(requests, 'req_auth.html')



def chek_number(requests):
    if requests.method == 'GET':
            text = requests.path.rstrip('/')
            reg = re.compile('[/]')
            t = reg.sub('', text)
            p = t.split('chek_number')
            new_text = p[0]
            item = []
            number = {}
            what = {}
            country = requests.GET['country']
            limit = requests.GET['limit']
            username = requests.user.username
            coun = numberssssq.objects.all()
            for i in coun:
                if i.shirt_size == country and i.bool_number == True:
                    items = company.objects.all()
                    for j in items:
                        if limit == 'Отключен':
                            if str(j.name_company) == str(i.shirt_company) and j not in item:
                                n = numberssssq.objects.filter(shirt_size=country, shirt_company=j.id, bool_number=True).count()
                                item.append(j)
                                number.setdefault(j.name_company, str(n))
                                what.setdefault(j.name_company, str(i.shirt_limit))
                        elif j.name_company == i.shirt_company and i.shirt_limit == limit and j not in item:
                            n = numberssssq.objects.filter(shirt_size=country, shirt_company=j.name_company, bool_number=True).count()
                            item.append(j)
                            number.setdefault(j.name_company, str(n))
                            what.setdefault(j.name_company, str(i.shirt_limit))
            url = '?'
            register_yes = 'yes'
            if requests.user.is_active:
                if new_text == '':
                    new_text = 'index'
                return render(requests, str(new_text)+'.html', {'username':username, 'ite':item, 'number':number, 'what':what, 'url':url, 'reqister':register_yes})
            else:
                if new_text == '':
                    new_text = 'index'
                return render(requests, str(new_text)+'.html',
                              {'username': username, 'ite': item, 'number': number, 'what': what, 'url': url})

def activeite(requests):
    if requests.user.is_active:
        username = requests.user.username
        idi = requests.user.id
        url = 'chek_number?'
        register_yes = 'yes'
        comp = company.objects.get(id=requests.GET['id'])
        number = numberssssq.objects.filter(shirt_company=comp, bool_number=True)
        for j in number:

            s = numberssssq.objects.get(number_phonesq=j.number_phonesq)
            s.bool_number = False
            s.save()
            save_number = numbers_of_phone(id_user=idi, phone=j.number_phonesq, company=j.shirt_company,
                                               price_number=comp.usasq)
            save_number.save()
            number = numbers_of_phone.objects.filter(id_user=requests.user.id).all()

            return render(requests, 'rent_number.html', {'username': username, 'phone_num': number, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'entrance.html')

def activeites(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'

        number = numbers_of_phone.objects.filter(id_user=requests.user.id).all()
        return render(requests, 'rent_number.html', {'username': username, 'phone_num': number, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'entrance.html')

def show_number(requests):
    if requests.method == 'GET':
            SHIRT_SIZES = {'KNK': 'Канада', 'USA': 'США', 'RUS': 'Россия', 'NDN': 'Нидерланды', 'FRF': 'Франция', 'ISI': 'Испания', 'ITI': 'Италия', 'AVA': 'Австрия', 'UKU': 'Англия', 'GER': 'Германия'}
            item = []
            number = {}
            what = {}
            country = requests.GET['country']
            con = SHIRT_SIZES[country]
            username = requests.user.username
            coun = numberssssq.objects.all()
            for i in coun:
                if i.shirt_size == country and i.bool_number == True:
                    items = company.objects.all()
                    for j in items:
                        print(j.name_company, i.shirt_company)
                        if str(j.name_company) == str(i.shirt_company) and j not in item:
                            n = numberssssq.objects.filter(shirt_size=country, shirt_company=j.id).count()
                            item.append(j)
                            number.setdefault(j.name_company, str(n))
                            what.setdefault(j.name_company, str(i.shirt_limit))
            url = '?'
            register_yes = 'yes'
            n = len(item)
            ur = '?'
            return render(requests, 'rent_active.html', {'username': username, 'url': url, 'reqister': register_yes, 'ites': item, 'numbers': number, 'n':n, 'ur':ur, 'contry':con})


def pay(requests):
    if requests.user.is_active:
        username = requests.user.username
        url = 'chek_number?'
        register_yes = 'yes'
        return render(requests, 'pay.html', {'username': username, 'url':url, 'reqister':register_yes})
    else:
        return render(requests, 'entrance.html')

def add_sms_to_bd(requests):
    if requests.method == 'GET':
        if numbers_of_phone.objects.filter(phone = requests.GET['num']):
            numbers_of_phone.objects.filter(phone = requests.GET['num']).update(sms_kod=requests.GET['sms'])