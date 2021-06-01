from django.shortcuts import render
import requests
import re
import json
import sys
import os

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        return True
    else:
        return False

def home(request):
    return render(request,'home.html')


def index(request):
    token = 'token'
    version = 5.129
    id = request.POST.get('param')
    fields = 'city,photo_400,occupation,career,relatives,schools,education,site,connections,contacts,has_mobile,about,bdate,home_town,military'
    payload = {'access_token': token, 'v': version, 'user_ids': id, 'fields': fields}
    response = requests.get('https://api.vk.com/method/users.get', params=payload)
    data = response.json()
    data_value = []
    for value in data.values():
        data_value.extend(value)
    user_data = {k: v for k, v in data_value[0].items() if v != ''}
    return render(request,'index.html',{'data': user_data})