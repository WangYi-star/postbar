# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2021/7/2 12:18
# Tool ：PyCharm

from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from app1.models import LoginModel, PostModel, ReplyModel, UserModel


from django import db
from django.db import connection
import time
import os

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
import base64
from django.contrib.auth.hashers import make_password,check_password


def usermanage(request):
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        if request.POST:
            username = request.POST.get("username")
            if username:
                gender = request.POST.get("gender")
                birthday = request.POST.get("birthday")
                sign = request.POST.get("sign")

                user_new = UserModel.objects.get(uid=uid)
                user_new.username = username
                user_new.gender = gender
                user_new.birthday = birthday
                user_new.sign = sign
                user_new.save()
                # # 后端实现触发器，级联修改post，reply
                # cursor = connection.cursor()
                # cursor.execute("update app1_postmodel set app1_postmodel.username=%s where app1_postmodel.uid=%s",[username,uid])
                # cursor.execute("update app1_replymodel set app1_replymodel.username = %s where app1_replymodel.uid=%s",[username,uid])
            else:
                occupation = request.POST.get("occupation")
                edress = request.POST.get("edress")
                phone = request.POST.get("phone")
                location = request.POST.get("location")
                userintro = request.POST.get("introduction")

                user_new = UserModel.objects.get(uid=uid)
                user_new.occupation = occupation
                user_new.edress = edress
                user_new.phone = phone
                user_new.location = location
                user_new.userintro = userintro
                user_new.save()
            return redirect("/usermanage")
        cursor = connection.cursor()
        cursor.execute("select u.username,u.gender,u.birthday,u.sign,u.occupation,u.edress,u.phone,u.location,u.userintro,u.filename from app1_usermodel as u where u.uid=%s", [uid, ])
        raw1 = cursor.fetchall()
        rname = raw1[0][9]
        if rname:
            filename = "/static/headportrait/"+rname
        else:
            filename = "/static/images/head.png"
        return render(request, "usermanage.html", {"uid": uid, "detail": raw1[0], "filename":filename})
    else:
        return HttpResponse("请先登录！")

def upload_fie(request):
    if request.POST:
        myfile = request.FILES.get("myfile", None)
        uid = request.GET.get("uid")
        if myfile:
            file_name, file_extension = os.path.splitext(myfile.name)
            if file_extension in ['.jpg','.jpeg','.png']:
                filename =request.GET.get("uid")+file_extension
                destination = open("./statics/headportrait/"+filename, 'wb+')
                for chunk in myfile.chunks():
                    destination.write(chunk)
                destination.close()
                cursor = connection.cursor()
                cursor.execute("update app1_usermodel set filename=%s where uid=%s", [filename, uid])
                return redirect("/usermanage")
            else:
                return HttpResponse('''<script>alert("请选择图片格式的文件！");window.location.href="/usermanage"</script>''')
        else:
            return HttpResponse('''<script>alert("请选择文件");window.location.href="/usermanage"</script>''')
    return redirect("/usermanage")

def upload_fie_bug(request):
    if request.POST:
        myfile = request.FILES.get("myfile", None)
        uid = request.GET.get("uid")
        if myfile:
            file_name, file_extension = os.path.splitext(myfile.name)
            filename =request.GET.get("uid")+file_extension
            destination = open("./statics/headportrait/"+filename, 'wb+')
            for chunk in myfile.chunks():
                destination.write(chunk)
            destination.close()
            cursor = connection.cursor()
            cursor.execute("update app1_usermodel set filename=%s where uid=%s", [filename, uid])
            return redirect("/usermanage")
        else:
            return HttpResponse('''<script>alert("请选择文件");window.location.href="/usermanage"</script>''')
    return redirect("/usermanage")


def display_file(request):
    cursor = connection.cursor()
    cursor.execute("select u.uid,u.username,u.filename from app1_usermodel as u")
    raws = cursor.fetchall()
    return render(request, "showportrait.html", {"raws": raws})


def download_file(request):
    file_para = request.GET.get("filepath")
    if ".." in file_para:
        return HttpResponse('''<script>alert("非法请求");window.location.href="/display";</script>''')
    else:
        filename = request.GET.get("filename")
        filepath = "./statics/"+file_para   # /download?filename=123.png&filepath=../logs/luffy.log
        # filepath = "./statics/headportrait/"+filename
        fp = open(filepath, 'rb')
        response = StreamingHttpResponse(fp)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Dispositon'] = 'attachment;filename="%s"' % filename
        return response
        fp.close()

    # return render(request, "showportrait.html")

def display_file_bug(request):
    cursor = connection.cursor()
    cursor.execute("select u.uid,u.username,u.filename from app1_usermodel as u")
    raws = cursor.fetchall()
    return render(request, "showportrait_bug.html", {"raws": raws})


def download_file_bug(request):
    filename = request.GET.get("filename")
    filepath = "./statics/"+request.GET.get("filepath")     # /download_bug?filename=123.png&filepath=../logs/luffy.log
    # filepath = "./statics/headportrait/"+filename
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Dispositon'] = 'attachment;filename="%s"' % filename
    return response
    fp.close()