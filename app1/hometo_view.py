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


# 存在漏洞，报错注入，布尔注入
def hometo_bug(request):
    postid = request.GET.get("postid")

    cursor = connection.cursor()
    # 帖子
    # cursor.execute("select p.postid,p.topic,p.uid,p.username,p.posttime,p.text from app1_postmodel as p where p.postid=%s", [postid, ])
    select = '''select p.postid,p.topic,p.uid,p.username,p.posttime,p.text from app1_postmodel as p where p.postid=''' +postid  # or updatexml (1,concat (0x7e,database()),0)
    cursor.execute(select)
    raw1 = cursor.fetchall()
    topic = raw1[0]
    # 回复 存在sql注入问题
    cursor.execute(
        "select r.uid,r.username,r.content,r.time from app1_replymodel as r where r.postid="+postid+" and r.delete=0 order by r.time desc ")
    raw2 = cursor.fetchall()

    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request,"hometo.html",{"replys":raw2, "topic":topic, "uid":uid, "postid":postid})
    else:
        return render(request,"hometo.html",{"replys":raw2, "topic":topic, "postid":postid})


# 修复漏洞，绕过特殊字符
def hometo(request):
    postid = request.GET.get("postid")
    key_word = ["updatexml", "concat", "and", "or", "#"]
    for i in key_word:
        if i in postid:
            return HttpResponse('''<script>alert("非法请求！")</script>''')
    cursor = connection.cursor()
    # 帖子
    # cursor.execute("select p.postid,p.topic,p.uid,p.username,p.posttime,p.text from app1_postmodel as p where p.postid=%s", [postid, ])
    select = '''select p.postid,p.topic,p.uid,p.username,p.posttime,p.text from app1_postmodel as p where p.postid=''' +postid  # or updatexml (1,concat (0x7e,database()),0)
    cursor.execute(select)
    raw1 = cursor.fetchall()
    topic = raw1[0]
    # 回复 存在sql注入问题
    cursor.execute(
        "select r.uid,r.username,r.content,r.time from app1_replymodel as r where r.postid="+postid+" and r.delete=0 order by r.time desc ")
    raw2 = cursor.fetchall()

    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        return render(request,"hometo.html",{"replys":raw2, "topic":topic, "uid":uid, "postid":postid})
    else:
        return render(request,"hometo.html",{"replys":raw2, "topic":topic, "postid":postid})



def commitreply(request):
    if request.POST:
        postid = request.GET.get("postid")
        uid = request.COOKIES.get("uid")
        # username
        cursor = connection.cursor()
        cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
        raw1 = cursor.fetchall()
        username = raw1[0][0]
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # order
        cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s", [postid, ])
        raw1 = cursor.fetchall()
        if raw1[0][0]:
            order = raw1[0][0]+1
        else:
            order = 1
        content = request.POST["message"]  # <script>window.open("https://www.baidu.com")</script>

        # 过滤特殊字符，解决XSS漏洞
        if "<script>" in content or "</script>" in content:
            return HttpResponse('''<script>alert("非法请求！");window.opener.location.href = window.opener.location.href;window.close();</script>''')
        ReplyModel(postid=postid, uid=uid, username=username, time=now_time, delete=0, order=order, content=content).save()
        return HttpResponse(content+'''<br><button onclick="window.opener.location.href = window.opener.location.href;window.close();">确定</button>''')
    else:
        is_login = request.COOKIES.get("is_login")
        if is_login:
            # uid = request.COOKIES.get("uid")
            return render(request, "commithometo.html")
        else:
            return HttpResponse("click to login!")


def commitreply_bug(request):
    if request.POST:
        postid = request.GET.get("postid")
        uid = request.COOKIES.get("uid")
        # username
        cursor = connection.cursor()
        cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
        raw1 = cursor.fetchall()
        username = raw1[0][0]
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # order
        cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s", [postid, ])
        raw1 = cursor.fetchall()
        if raw1[0][0]:
            order = raw1[0][0]+1
        else:
            order = 1
        content = request.POST["message"]  # <script>window.open("https://www.baidu.com")</script>
        ReplyModel(postid=postid, uid=uid, username=username, time=now_time, delete=0, order=order, content=content).save()
        return HttpResponse(content+'''<br><button onclick="window.opener.location.href = window.opener.location.href;window.close();">确定</button>''')
    else:
        is_login = request.COOKIES.get("is_login")
        if is_login:
            # uid = request.COOKIES.get("uid")
            return render(request, "commithometo.html")
        else:
            return HttpResponse("click to login!")
