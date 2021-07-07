# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2021/7/2 16:55
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



def postmanage(request):
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        postall = PostModel.objects.filter(uid=uid).order_by("-posttime")
        # return HttpResponse(postall[0].topic)
        return render(request, "post.html", {"uid": uid, "postall":postall})
    else:
        return HttpResponse("请先登录！")

def replymanage(request):
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        identity = request.COOKIES.get("identity")
        merge = str(uid)+str(identity)
        identity_verify = request.COOKIES.get("identity_verify")
        merge_encode = base64.b64encode(merge.encode())
        if str(identity_verify) == str(merge_encode):  # 验证cookie：uid、identity是否被修改
            if identity == "admin":
                cursor = connection.cursor()
                cursor.execute(
                    "select p.topic,r.content,r.time,r.replyid,p.postid from app1_postmodel as p, app1_replymodel as r where r.postid=p.postid and r.delete=0 order by r.time desc")
            else:
                cursor = connection.cursor()
                cursor.execute(
                    "select p.topic,r.content,r.time,r.replyid,p.postid from app1_postmodel as p, app1_replymodel as r where r.uid=%s and r.postid=p.postid and r.delete=0 order by r.time desc",
                    [uid, ])
            replyall = cursor.fetchall()
            return render(request, "reply.html", {"uid": uid, "replyall": replyall})
        else:
            return HttpResponse('''<script>alert("非法请求！cookie被修改");window.location.href="/home"</script>''')
    else:
        return HttpResponse("请先登录！")

def replymanage_bug(request):
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        identity = request.COOKIES.get("identity")
        if identity == "admin":
            cursor = connection.cursor()
            cursor.execute("select p.topic,r.content,r.time,r.replyid,p.postid from app1_postmodel as p, app1_replymodel as r where r.postid=p.postid and r.delete=0 order by r.time desc")
        else:
            cursor = connection.cursor()
            cursor.execute("select p.topic,r.content,r.time,r.replyid,p.postid from app1_postmodel as p, app1_replymodel as r where r.uid=%s and r.postid=p.postid and r.delete=0 order by r.time desc", [uid, ])
        replyall = cursor.fetchall()
        return render(request, "reply.html", {"uid": uid, "replyall": replyall})
    else:
        return HttpResponse("请先登录！")


# 根据留言的ID删除
def delreply(request):   # 修复了 水平越权的bug
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        uid_verify = request.COOKIES.get("uid_verify")
        uid_encode = base64.b64encode(uid.encode())
        if str(uid_verify) != str(uid_encode): # 验证cookie：uid是否被修改
            return HttpResponse('''<script>alert("非法请求！cookie被修改");window.location.href="/home"</script>''')
        del_id = request.GET.get("del_id")
        post_id = request.GET.get("belong_postid")
        reply = ReplyModel.objects.get(replyid=del_id)
        if reply.uid != uid:
            return HttpResponse("非法请求！此用户没有权限")
        reply.delete = 1
        reply.save()

        # 级联修改postmodel的number和recent字段
        post = PostModel.objects.get(postid=post_id)
        if(post.number == 1):
            post.recent = 0
        else:
            cursor = connection.cursor()
            cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s and r.delete=0", [post_id, ])
            raw1 = cursor.fetchall()
            post.recent = raw1[0][0]
        post.number = post.number-1
        post.save()
        return redirect("/replymanage")
    else:
        return HttpResponse("请先登录！")

def delreply_bug(request):    # 存在水平越权的bug
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        del_id = request.GET.get("del_id")
        post_id = request.GET.get("belong_postid")
        reply = ReplyModel.objects.get(replyid=del_id)
        if reply.uid != uid:
            return HttpResponse('''<script>alert("非法请求！");</script>''')
        reply.delete = 1
        reply.save()
        # 级联修改postmodel的number和recent字段
        post = PostModel.objects.get(postid=post_id)
        if(post.number == 1):
            post.recent = 0
        else:
            cursor = connection.cursor()
            cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s and r.delete=0", [post_id, ])
            raw1 = cursor.fetchall()
            post.recent = raw1[0][0]
        post.number = post.number-1
        post.save()
        return redirect("/home")
    else:
        return HttpResponse("请先登录！")

def delreply_identity(request):   # 修复了 水平越权的bug
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        identity = request.COOKIES.get("identity")
        # return HttpResponse(str(uid)+str(identity))
        merge = str(uid)+str(identity)
        identity_verify = request.COOKIES.get("identity_verify")
        merge_encode = base64.b64encode(merge.encode())
        if str(identity_verify) != str(merge_encode): # 验证cookie：uid、identity是否被修改
            return HttpResponse('''<script>alert("非法请求！cookie被修改");window.location.href="/home"</script>''')
        del_id = request.GET.get("del_id")
        post_id = request.GET.get("belong_postid")
        reply = ReplyModel.objects.get(replyid=del_id)
        if identity == "admin" or reply.uid == uid:
            reply.delete = 1
            reply.save()

            # 级联修改postmodel的number和recent字段
            post = PostModel.objects.get(postid=post_id)
            if(post.number == 1):
                post.recent = 0
            else:
                cursor = connection.cursor()
                cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s and r.delete=0", [post_id, ])
                raw1 = cursor.fetchall()
                post.recent = raw1[0][0]
            post.number = post.number-1
            post.save()
            return redirect("/home")
        else:
            return HttpResponse("非法请求！此用户没有权限")
    else:
        return HttpResponse("请先登录！")

def delreply_identity_bug(request):    # 存在水平越权的bug
    is_login = request.COOKIES.get("is_login")
    if is_login:
        uid = request.COOKIES.get("uid")
        identity = request.COOKIES.get("identity")
        del_id = request.GET.get("del_id")
        post_id = request.GET.get("belong_postid")
        reply = ReplyModel.objects.get(replyid=del_id)
        # if reply.uid != uid and identity!="admin":
        #     return HttpResponse('''<script>alert("非法请求！");</script>''')
        if identity == "admin" or reply.uid == uid:
            reply.delete = 1
            reply.save()
            # 级联修改postmodel的number和recent字段
            post = PostModel.objects.get(postid=post_id)
            if(post.number == 1):
                post.recent = 0
            else:
                cursor = connection.cursor()
                cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s and r.delete=0", [post_id, ])
                raw1 = cursor.fetchall()
                post.recent = raw1[0][0]
            post.number = post.number-1
            post.save()
            return redirect("/home")
        else:
            return HttpResponse('''<script>alert("非法请求！");</script>''')
    else:
        return HttpResponse("请先登录！")
