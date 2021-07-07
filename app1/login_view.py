# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2021/7/2 10:16
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

# SQL注入漏洞        5.

# '#'注释跳过登录
def login_bug(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        select = "select * from app1_loginmodel as r where r.uid= '"+uid+"' and r.password='"+password+"'"
        cursor = connection.cursor()
        cursor.execute(select)
        raw1 = cursor.fetchall()
        if(len(raw1) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/home/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", raw1[0][0])
            return rep
    return render(request, "login.html")


# 修复SQL注入（“#”注释）漏洞,存在其他安全漏洞，默认的登录入口   5.
def login(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        # user_all = LoginModel.objects.all()
        # booltype = check_password("123456", password)
        # user = LoginModel.objects.filter(uid=uid).filter(password=password)
        # user = LoginModel.objects.filter(uid=uid).all()
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/home/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", user[0].uid)
            return rep
    return render(request, "login.html")

# 修复身份验证漏洞，添加uid校验码
def login_verify(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/home_verify_uid/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", uid)
            uid_verify = base64.b64encode(uid.encode())
            rep.set_cookie("uid_verify", uid_verify)
            return rep
    return render(request, "login.html")


def login_verify_identity(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/home_verify_uid/')
            identity = user[0].identity
            rep.set_cookie("is_login", True)
            rep.set_cookie("identity", identity)
            rep.set_cookie("uid", uid)
            merge = uid+identity
            uid_verify = base64.b64encode(uid.encode())
            identity_verify = base64.b64encode(merge.encode())
            rep.set_cookie("uid_verify", uid_verify)
            rep.set_cookie("identity_verify", identity_verify)
            return rep
    return render(request, "login.html")



# 修复身份验证漏洞，添加uid校验码
def login_verify_bug(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/home_verify_uid_bug/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", uid)
            return rep
    return render(request, "login.html")



# 双因子验证 漏洞
def login_first_bug(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/login_second_bug')
            rep.set_cookie("uid", uid)
            return rep
    return render(request, "login.html")

def login_second_bug(request):
    if request.POST:
        verify = request.POST.get("verify")
        if verify == "123456":
            uid = request.COOKIES.get("uid")
            rep = redirect('/home/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", uid)
            return rep
        else:
            return ("登陆失败！")
    else:
        return render(request, "login_verify.html")

# 双因子验证 修复
def login_first(request):
    if request.POST:
        uid = request.POST['uid']
        password = request.POST['password']
        user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
        if (len(user) == 0):
            return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
        else:
            rep = redirect('/login_second')
            rep.set_cookie("uid", uid)
            uid_verify = base64.b64encode(uid.encode())
            rep.set_cookie("uid_verify", uid_verify)
            return rep
    return render(request, "login.html")

def login_second(request):
    if request.POST:
        verify = request.POST.get("verify")
        uid_verify = request.COOKIES.get("uid_verify")
        uid = request.COOKIES.get("uid")
        encode_uid = base64.b64encode(uid.encode())
        if verify == "123456" and str(encode_uid) == str(uid_verify):
            rep = redirect('/home/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", uid)
            return rep
        else:
            return HttpResponse("登陆失败！")
    else:
        return render(request, "login_verify.html")

# 修复其它安全漏洞，密码加密传输，验证码防止暴力破解密码    9.
def login_rsa(request):
    if request.POST:
        uid = request.POST.get('uid')
        # 经过加密的密码，str格式
        password = request.POST.get('password')
        # return HttpResponse(password)

        # 使用存储的私钥进行解密
        # 1.从session获取
        # privkeystr = request.session.get('privkey').encode()
        # 2.从文件获取，privkeystr为pcks#1格式，bytes
        with open('private/my_private_rsa_key.pem', 'r') as f:
            privkeystr = f.read().encode()
            f.close()
        # privkey 为私钥对象，由n，e等数字构成
        privkey = RSA.importKey(privkeystr)
        cipher = PKCS1_v1_5.new(privkey)
        # 现将base64编码格式的password解码，然后解密，并用decode转成str
        password = cipher.decrypt(base64.b64decode(password.encode()), 'error').decode()
        # 至此，password解密成功，省略后面验证用户名和密码的代码了。

        user = LoginModel.objects.filter(uid=uid).first()
        booltype = check_password(password, user.password)
        if booltype:
            rep = redirect('/home/')
            rep.set_cookie("is_login", True)
            rep.set_cookie("uid", uid)
            return rep
        else:
            return HttpResponse('''<script>alert("用户名或密码错误！");window.location.href="/loginrsa"</script>''')
    else:
        # 伪随机数方式生成RSA公私钥对
        random_generator = Random.new().read
        rsa = RSA.generate(1024, random_generator)
        rsa_private_key = rsa.exportKey()
        rsa_public_key = rsa.publickey().exportKey()
        # 1. 以session的方式存储私钥，PKCS1格式
        # request.session['privkey'] = rsa_private_key.decode()
        # 2. 存储到静态文件
        with open('private/my_private_rsa_key.pem', 'w+') as f:
            f.write(rsa_private_key.decode())
            f.close()
        # return render(request, 'loginrsa.html', {'pub_key': rsa_public_key.decode()})
        return render(request, 'loginpage.html', {'pub_key': rsa_public_key.decode()})

# 登出
def logout(request):
    rep = redirect('/home')
    rep.delete_cookie("is_login")
    return rep


# 注册, 密码加密存储，密码强度约束   9.
def register(request):
    if request.POST:
        uid = request.POST.get("uid")
        cursor = connection.cursor()
        cursor.execute("select * from app1_loginmodel where uid = %s", [uid, ])
        raws = cursor.fetchall()
        if(len(raws)==0):
            password = request.POST.get("password")
            encrypt_password = make_password(password)
            cursor.execute("insert into app1_loginmodel values(%s,%s)", [uid, encrypt_password])
            return HttpResponse('''<script>alert("注册成功，返回登录！");window.location.href="/login"</script>''')
        else:
            return HttpResponse('''<script>alert("该用户ID已注册！");window.location.href="/register"</script>''')
    else:
        return render(request, "register.html")