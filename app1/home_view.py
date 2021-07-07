# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2021/7/2 10:32
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
from django.utils.safestring import mark_safe

# 主页
def home(request):
    # 查找数据库
    cursor = connection.cursor()
    # cursor.execute("select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p,app1_replymodel as r where p.postid=r.postid and p.recent=r.order")
    cursor.execute(
        "select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p LEFT OUTER JOIN app1_replymodel as r on(p.postid=r.postid and p.recent=r.order) order by p.posttime desc ")
    raw = cursor.fetchall()
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request, "home.html", {"blogs": raw, "uid":uid})
    else:
        return render(request, "home.html", {"blogs": raw})


# 主页
def home_bug(request):
    # 查找数据库
    cursor = connection.cursor()
    # cursor.execute("select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p,app1_replymodel as r where p.postid=r.postid and p.recent=r.order")
    cursor.execute(
        "select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p LEFT OUTER JOIN app1_replymodel as r on(p.postid=r.postid and p.recent=r.order) order by p.posttime desc ")
    raw = cursor.fetchall()
    post_list = []
    for element in raw:
        new_list = []
        new_list.append(element[0])
        new_list.append(mark_safe(element[1]))
        new_list.append(element[2])
        new_list.append(element[3])
        new_list.append(element[4])
        new_list.append(element[5])
        new_list.append(element[6])
        post_list.append(new_list)
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request, "home.html", {"blogs": raw, "uid": uid})
    else:
        return render(request, "home.html", {"blogs": post_list})


# 主页
def home_verify_uid(request):
    # 查找数据库
    cursor = connection.cursor()
    # cursor.execute("select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p,app1_replymodel as r where p.postid=r.postid and p.recent=r.order")
    cursor.execute(
        "select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p LEFT OUTER JOIN app1_replymodel as r on(p.postid=r.postid and p.recent=r.order) order by p.posttime desc ")
    raw = cursor.fetchall()
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request, "home_verify_uid.html", {"blogs": raw, "uid": uid})
    else:
        return render(request, "home_verify_uid.html", {"blogs": raw})

# 主页
def home_verify_uid_bug(request):
    # 查找数据库
    cursor = connection.cursor()
    # cursor.execute("select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p,app1_replymodel as r where p.postid=r.postid and p.recent=r.order")
    cursor.execute(
        "select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p LEFT OUTER JOIN app1_replymodel as r on(p.postid=r.postid and p.recent=r.order) order by p.posttime desc ")
    raw = cursor.fetchall()
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request, "home_verify_uid_bug.html", {"blogs": raw, "uid":uid})
    else:
        return render(request, "home_verify_uid.html_bug", {"blogs": raw})


# 跨镇请求伪造漏洞修复，添加csrf校验码    header注入，报错显示数据库名
def commitpost(request):
    if request.POST:
        topic = request.POST["topic"]
        uid = request.COOKIES.get("uid")
        uid = uid.replace("%20", " ")
        key_word = ["updatexml", "concat", "and", "or", "#"]
        for i in key_word:
            if i in uid:
                return HttpResponse('''<script>alert("非法请求！");window.opener.location.reload();window.close();</script>''')
        form_csrf = request.POST['form_csrf']
        cookie_csrf = request.COOKIES.get("cookie_csrf")
        if form_csrf == cookie_csrf:
            # username
            cursor = connection.cursor()
            # cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
            select = '''select u.username from app1_usermodel as u where u.uid="'''+uid +'''"''' #    " or updatexml(1,concat(0x7e,database()),0)#
            cursor.execute(select)
            raw1 = cursor.fetchall()
            username = raw1[0][0]
            posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            text = request.POST["message"]
            PostModel(topic=topic, uid=uid, username=username, posttime=posttime, recent=0, number=0, text=text).save()
            return HttpResponse('''	<script>
                alert("提交成功post!")
                window.opener.location.reload();
                window.close();
                </script>
                ''')
        else:
            return HttpResponse('''<script>alert("非法请求!")</script>''')
        # # username
        # cursor = connection.cursor()
        # cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
        # raw1 = cursor.fetchall()
        # username = raw1[0][0]
        # posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # text = request.POST["message"]
        # PostModel(topic=topic, uid=uid, username=username, posttime=posttime, recent=0, number=0, text=text).save()
        # return HttpResponse('''	<script>
        #     alert("提交成功post!")
        #     window.opener.location.reload();
        #     window.close();
        #     </script>
        #     ''')
    else:
        is_login = request.COOKIES.get("is_login")
        if is_login:
            csrf_token = bytes.decode(base64.b64encode(os.urandom(48)))
            # csrf_token = "110"
            rep = render(request, "commithome.html" , {"form_csrf": csrf_token})
            rep.set_cookie("cookie_csrf", csrf_token)
            return rep
            # return render(request, "commithome.html" , csrf_token=csrf_token)
        else:
            return HttpResponse("click to login!")


# 跨站请求漏洞，没有csrf校验码，可从攻击网站提交表单数据
def commitpost_bug(request):
    if request.POST:
        topic = request.POST["topic"]
        uid = request.COOKIES.get("uid")
        uid = uid.replace("%20", " ")
        # username
        cursor = connection.cursor()
        select = '''select u.username from app1_usermodel as u where u.uid="''' + uid + '''"'''  # " or updatexml(1,concat(0x7e,database()),0)#
        cursor.execute(select)
        # cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
        raw1 = cursor.fetchall()
        username = raw1[0][0]
        posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = request.POST["message"]
        PostModel(topic=topic, uid=uid, username=username, posttime=posttime, recent=0, number=0, text=text).save()
        return HttpResponse('''	<script>
            alert("提交成功post!")
            window.opener.location.reload();
            window.close();
            </script>
            ''')
    else:
        is_login = request.COOKIES.get("is_login")
        if is_login:
            return render(request, "commithome.html")
        else:
            return HttpResponse("click to login!")


def commitpost_verify_uid(request):   # 9.模拟其他用户发帖
    if request.POST:
        topic = request.POST["topic"]
        uid = request.COOKIES.get("uid")
        uid_verify = request.COOKIES.get("uid_verify")
        uid_encode = base64.b64encode(uid.encode())
        if str(uid_verify) != str(uid_encode):
            return HttpResponse('''<script>alert("非法请求！");window.opener.location.reload();window.close();</script>''')
        # username
        cursor = connection.cursor()
        select = '''select u.username from app1_usermodel as u where u.uid="''' + uid + '''"'''  # " or updatexml(1,concat(0x7e,database()),0)#
        cursor.execute(select)
        # cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
        raw1 = cursor.fetchall()
        username = raw1[0][0]
        posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = request.POST["message"]
        PostModel(topic=topic, uid=uid, username=username, posttime=posttime, recent=0, number=0, text=text).save()
        return HttpResponse('''	<script>
            alert("提交成功post!")
            window.opener.location.reload();
            window.close();
            </script>
            ''')
    else:
        is_login = request.COOKIES.get("is_login")
        if is_login:
            return render(request, "commithome.html")
        else:
            return HttpResponse("click to login!")

