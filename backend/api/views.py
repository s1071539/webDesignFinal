from django.shortcuts import render
from .models import Users, Test, Product
# Create your views here.
from django.http import HttpResponse
import json
import copy
import sys
sys.path.append("..")#為了呼叫上級py檔案函式
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
import os
from copy import copy
from datetime import datetime, timedelta, timezone
from io import BytesIO

from openpyxl import Workbook
from openpyxl.styles import Border, Side, Alignment
import time
import smtplib
import variable

#-------------------login------------------------#
@csrf_exempt
def login(request):
    '''登入資料核對及回傳資料'''
    user = json.loads(request.GET['user'])
    if Users.objects.filter(user=user[0]):
        if user[1] == Users.objects.get(user=user[0]).password:
            return HttpResponse('{"msg":"登入成功!"}')
        else:
            return HttpResponse('{"msg":"密碼錯誤!"}')
    else: 
        return HttpResponse('{"msg":"登入失敗，無此帳號!"}')




#-------------------user------------------------#
@csrf_exempt
def add_user_prize(request):
    user = json.loads(request.body)['user']
    prize_info = json.loads(request.body)['prize_info']
    if(Users.objects.get(user=user).record != ''):
        user_prize = json.loads(Users.objects.get(user=user).record)
    else:
        user_prize = []
    
    user_prize.append(prize_info)
    Users.objects.filter(user=user).update(record=json.dumps(user_prize))
    return HttpResponse("獎品更新成功")

@csrf_exempt
def get_user_prize(request):
    user = json.loads(request.body)['user']
    user_prize = Users.objects.get(user=user).record
    return HttpResponse(json.dumps(user_prize))

@csrf_exempt
def del_user_prize(request):
    user = json.loads(request.body)['user']
    prize_info = json.loads(request.body)['prize_info']
    user_prize = Users.objects.get(user=user).record
    if user_prize != '':
        user_prize = json.loads(user_prize)


    left_prize = []
    for i in range(len(prize_info)):
        if prize_info[i] == False:
            left_prize.append(user_prize[i])
    print(left_prize)
    Users.objects.filter(user=user).update(record=json.dumps(left_prize))
    return HttpResponse("獎品更新成功")

@csrf_exempt
def set_user_money(request):
    user = json.loads(request.body)['user']
    add_money = json.loads(request.body)['money']
    current_money = Users.objects.get(user=user).setting
    if current_money == "X" or current_money == "x":
        total_money = int(add_money)
    else:
        total_money =  int(current_money) + int(add_money)
    Users.objects.filter(user=user).update(setting=total_money)
    return HttpResponse("加值成功")

@csrf_exempt
def get_all_user(request):
    user_data = []
    for user in Users.objects.all():
        user_data.append({'user_id':user.user_id,'user':user.user,'password':user.password,'email':user.email,'record':user.record,'description':user.description,'setting':user.setting})
    return HttpResponse(json.dumps(user_data))

@csrf_exempt
def operator_user(request):
    operator = (request.GET['operator'])
    if operator == "add":
        form = ( json.loads(request.GET['form']))
        for i in range(1,len(Users.objects.all())+2):
            if not Users.objects.filter(user_id = i):
                Users.objects.create(
                    user_id = i,
                    user = form['user'],
                    password = form['password'],
                    email = form['email'],
                    groups = form['groups'],
                    region = form['region'],
                    record = "",
                    description = form['description'],
                    setting = 0,
                )
                break
        return HttpResponse('成功新增使用者')
    elif operator == "modify":
        form = ( json.loads(request.GET['form']))
        Users.objects.filter(user_id = form['id']).update(
            user = form['user'],
            password = form['password'],
            email = form['email'],
        )
        return HttpResponse('成功修改使用者')
    elif operator == "delete":
        user_id = ( json.loads(request.GET['user_id']))
        Users.objects.filter(user_id = user_id).delete()
        return HttpResponse('成功刪除使用者')

    
#-------------------product------------------------#
@csrf_exempt
def operator_product(request):
    operator = (request.GET['operator'])
    if operator == "add":
        form = json.loads(request.GET['form'])
        new_id = 0
        for i in range(1, len(Product.objects.all())+2):
            if not Product.objects.filter(id = i):
                new_id = i
                Product.objects.create(#將修改的資料放入資料庫
                    id = i,
                    name = form['name'],
                    price = form['price'],
                    amount = form['amount'],
                    hot = 0,
                    time = form['time'],
                    owner = form['owner'],
                    group = form['group'],
                    url = "",
                )
                break
                
       
        return HttpResponse({new_id})
    elif operator == "modify":
        form = ( json.loads(request.GET['form']))
        Product.objects.filter(id = form['id']).update(
            name = form['name'],
            price = form['price'],
            amount = form['amount'],
            hot = form['hot'],
            time = form['time'],
        )
        return HttpResponse('成功修改商品')
    elif operator == "delete":
        product_id = ( json.loads(request.GET['id']))
        Product.objects.filter(id = product_id).delete()
        return HttpResponse('成功刪除商品')


@csrf_exempt
def get_all_product(request):
    product_data = []
    for product in Product.objects.all():
        product_data.append({'id':product.id ,'name':product.name,'price':product.price, 'amount':product.amount, 'hot':product.hot, 'time':product.time, 'owner':product.owner, 'group':product.group, 'url':''})

    return HttpResponse(json.dumps(product_data))

@csrf_exempt
def get_all_product_url(request):
    product_data = []
    for product in Product.objects.all():
        product_data.append(product.url)

    return HttpResponse(json.dumps(product_data))

@csrf_exempt
def add_product_url(request):
    data = json.loads(request.body)
    Product.objects.filter(id = data['new_id']).update(
        url = json.loads(data['url'])
    )
    return HttpResponse('成功上傳照片')