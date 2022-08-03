from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    # список всех букв англ алфавита
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # условие по настройке регистра
    if request.GET.get('uppercase'): # значение в get берем из password.html
        # extend - добавления каждого элемента итерируемого в конец текущего списка
        characters.extend(list('ABCDEFGHIJKLMNOPQSTUVWXYZ'))

    if request.GET.get('special'):
        # extend - добавления каждого элемента итерируемого в конец текущего списка
        characters.extend(list('!@#$%ˆ&*()'))

    if request.GET.get('numbers'):
        # extend - добавления каждого элемента итерируемого в конец текущего списка
        characters.extend(list('0123456789'))

    # задаем длину пароля
    length = int(request.GET.get('length', 12))  # теперь он будет брать значение из нашего запроса в адресной строке
    # default 12

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
