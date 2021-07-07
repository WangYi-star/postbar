
# Create your views here.

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

def hello(request):
    return render(request, "verifycode.html")



def prac(request):
    reply = "<script>alert(120)</script>"
    html_reply = mark_safe(reply)
    return render(request, "prac.html", {"reply": html_reply})
    # return HttpResponse(reply)

# def home(request):
#     # 查找数据库
#     cursor = connection.cursor()
#     # cursor.execute("select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p,app1_replymodel as r where p.postid=r.postid and p.recent=r.order")
#     cursor.execute(
#         "select p.number,p.topic,p.username,p.posttime,r.time,r.username,p.postid as number from app1_postmodel as p LEFT OUTER JOIN app1_replymodel as r on(p.postid=r.postid and p.recent=r.order) order by p.posttime desc ")
#     raw = cursor.fetchall()
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         return render(request, "home.html", {"blogs": raw, "uid":uid})
#     else:
#         return render(request, "home.html", {"blogs": raw})


# def hometo(request):
#     postid = request.GET.get("postid")
#
#     cursor = connection.cursor()
#     # 帖子
#     cursor.execute("select p.postid,p.topic,p.uid,p.username,p.posttime,p.text from app1_postmodel as p where p.postid=%s", [postid, ])
#     raw1 = cursor.fetchall()
#     topic = raw1[0]
#     # 回复 存在sql注入问题
#     cursor.execute(
#         "select r.uid,r.username,r.content,r.time from app1_replymodel as r where r.postid="+postid+" and r.delete=0 order by r.time desc ")
#     raw2 = cursor.fetchall()
#
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         return render(request,"hometo.html",{"replys":raw2, "topic":topic, "uid":uid, "postid":postid})
#     else:
#         return render(request,"hometo.html",{"replys":raw2, "topic":topic, "postid":postid})




# def commitpost(request):
#     if request.POST:
#         topic = request.POST["topic"]
#         uid = request.COOKIES.get("uid")
#         # username
#         cursor = connection.cursor()
#         cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
#         raw1 = cursor.fetchall()
#         username = raw1[0][0]
#         posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         text = request.POST["message"]
#         PostModel(topic=topic, uid=uid, username=username, posttime=posttime, recent=0, number=0, text=text).save()
#         return HttpResponse('''	<script>
#             alert("提交成功post!")
#             window.opener.location.reload();
#             window.close();
#             </script>
#             ''')
#     else:
#         is_login = request.COOKIES.get("is_login")
#         if is_login:
#             return render(request, "commithome.html")
#         else:
#             return HttpResponse("click to login!")
#
#
# def commitpost_csrf(request):
#     return render(request, "csrf_commitpost.html")


# def commitreply(request):
#     if request.POST:
#         postid = request.GET.get("postid")
#         uid = request.COOKIES.get("uid")
#         # username
#         cursor = connection.cursor()
#         cursor.execute("select u.username from app1_usermodel as u where u.uid=%s", [uid, ])
#         raw1 = cursor.fetchall()
#         username = raw1[0][0]
#         now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
#         # order
#         cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s", [postid, ])
#         raw1 = cursor.fetchall()
#         if raw1[0][0]:
#             order = raw1[0][0]+1
#         else:
#             order = 1
#         content = request.POST["message"]  # <script>window.open("https://www.baidu.com")</script>
#         return HttpResponse(content+'''<br><button onclick="window.opener.location.href = window.opener.location.href;window.close();">确定</button>''')
#         # ReplyModel(postid=postid, uid=uid, username=username, time=now_time, delete=0, order=order, content=content).save()
#         # return HttpResponse('''	<script>
#         #     alert("提交成功!")
#         #     window.opener.location.href = window.opener.location.href;
#         #     window.close();</script>
#         #     ''')
#     else:
#         is_login = request.COOKIES.get("is_login")
#         if is_login:
#             # uid = request.COOKIES.get("uid")
#             return render(request, "commithometo.html")
#         else:
#             return HttpResponse("click to login!")


# def usermanage(request):
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         if request.POST:
#             username = request.POST.get("username")
#             if username:
#                 gender = request.POST.get("gender")
#                 birthday = request.POST.get("birthday")
#                 sign = request.POST.get("sign")
#
#                 user_new = UserModel.objects.get(uid=uid)
#                 user_new.username = username
#                 user_new.gender = gender
#                 user_new.birthday = birthday
#                 user_new.sign = sign
#                 user_new.save()
#                 # # 后端实现触发器，级联修改post，reply
#                 # cursor = connection.cursor()
#                 # cursor.execute("update app1_postmodel set app1_postmodel.username=%s where app1_postmodel.uid=%s",[username,uid])
#                 # cursor.execute("update app1_replymodel set app1_replymodel.username = %s where app1_replymodel.uid=%s",[username,uid])
#             else:
#                 occupation = request.POST.get("occupation")
#                 edress = request.POST.get("edress")
#                 phone = request.POST.get("phone")
#                 location = request.POST.get("location")
#                 userintro = request.POST.get("introduction")
#
#                 user_new = UserModel.objects.get(uid=uid)
#                 user_new.occupation = occupation
#                 user_new.edress = edress
#                 user_new.phone = phone
#                 user_new.location = location
#                 user_new.userintro = userintro
#                 user_new.save()
#             return redirect("/usermanage")
#         cursor = connection.cursor()
#         cursor.execute("select u.username,u.gender,u.birthday,u.sign,u.occupation,u.edress,u.phone,u.location,u.userintro,u.filename from app1_usermodel as u where u.uid=%s", [uid, ])
#         raw1 = cursor.fetchall()
#         rname = raw1[0][9]
#         if rname:
#             filename = "/static/headportrait/"+rname
#         else:
#             filename = "/static/images/head.png"
#         return render(request, "usermanage.html", {"uid": uid, "detail": raw1[0], "filename":filename})
#     else:
#         return HttpResponse("请先登录！")
#
# def upload_fie(request):
#     if request.POST:
#         myfile = request.FILES.get("myfile", None)
#         uid = request.GET.get("uid")
#         if myfile:
#             filename =request.GET.get("uid")+".jpeg"
#             destination = open("./statics/headportrait/"+filename, 'wb+')
#             for chunk in myfile.chunks():
#                 destination.write(chunk)
#             destination.close()
#             cursor = connection.cursor()
#             cursor.execute("update app1_usermodel set filename=%s where uid=%s", [filename, uid])
#             return redirect("/usermanage")
#         else:
#             return HttpResponse('''<script>alert("请选择文件");window.location.href="/usermanage"</script>''')
#     return redirect("/usermanage")
#
# def display_file(request):
#     cursor = connection.cursor()
#     cursor.execute("select u.uid,u.username,u.filename from app1_usermodel as u")
#     raws = cursor.fetchall()
#     return render(request, "showportrait.html", {"raws": raws})
#
# def download_file(request):
#     filename = request.GET.get("filename")
#     filepath = "./statics/"+request.GET.get("filepath")
#     # filepath = "./statics/headportrait/"+filename
#     fp = open(filepath, 'rb')
#     response = StreamingHttpResponse(fp)
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Dispositon'] = 'attachment;filename="%s"' % filename
#     return response
#     fp.close()
#
#     # return render(request, "showportrait.html")

# def postmanage(request):
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         postall = PostModel.objects.filter(uid=uid).order_by("-posttime")
#         # return HttpResponse(postall[0].topic)
#         return render(request, "post.html", {"uid": uid, "postall":postall})
#     else:
#         return HttpResponse("请先登录！")
#
# def replymanage(request):
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         cursor = connection.cursor()
#         cursor.execute("select p.topic,r.content,r.time,r.replyid,p.postid from app1_postmodel as p, app1_replymodel as r where r.uid=%s and r.postid=p.postid and r.delete=0 order by r.time desc", [uid, ])
#         replyall = cursor.fetchall()
#         return render(request, "reply.html", {"uid": uid, "replyall":replyall})
#     else:
#         return HttpResponse("请先登录！")
#
# # 根据留言的ID删除
# def delreply(request):
#     is_login = request.COOKIES.get("is_login")
#     if is_login:
#         uid = request.COOKIES.get("uid")
#         del_id = request.GET.get("del_id")
#         post_id = request.GET.get("belong_postid")
#         reply = ReplyModel.objects.get(replyid=del_id)
#         reply.delete = 1
#         reply.save()
#
#         # 级联修改postmodel的number和recent字段
#         post = PostModel.objects.get(postid=post_id)
#         if(post.number == 1):
#             post.recent = 0
#         else:
#
#             cursor = connection.cursor()
#             cursor.execute("select MAX(r.order) from app1_replymodel as r where r.postid=%s and r.delete=0", [post_id, ])
#             raw1 = cursor.fetchall()
#             post.recent = raw1[0][0]
#         post.number = post.number-1
#         post.save()
#         return redirect("/replymanage")
#     else:
#         return HttpResponse("请先登录！")
#
#









# def login(request):
#     if request.POST:
#         uid = request.POST['uid']
#         password = request.POST['password']
#         # user_all = LoginModel.objects.all()
#         # booltype = check_password("123456", password)
#         # user = LoginModel.objects.filter(uid=uid).filter(password=password)
#         # user = LoginModel.objects.filter(uid=uid).all()
#         user = LoginModel.objects.filter(uid=uid).filter(password=password).all()
#         if (len(user) == 0):
#             return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
#         else:
#             rep = redirect('/home/')
#             rep.set_cookie("is_login", True)
#             rep.set_cookie("uid", user[0].uid)
#             return rep
#     return render(request, "login.html")
#
#
#     #     if(len(user) == 0):
#     #         return HttpResponse('''<a  href="/login">用户名错误，请重新登录！</a>''')
#     #     else:
#     #         booltype = check_password(password, user[0].password)
#     #         if booltype:
#     #             rep = redirect('/home/')
#     #             rep.set_cookie("is_login", True)
#     #             rep.set_cookie("uid", uid)
#     #             return rep
#     #         else:
#     #             return HttpResponse(" the password is wrong!")
#     # return render(request, "login.html")
#
#
# def login_rsa(request):
#     if request.POST:
#         name = request.POST.get('name')
#         # 经过加密的密码，str格式
#         password = request.POST.get('password')
#         # return HttpResponse(password)
#
#         # 使用存储的私钥进行解密
#         # 1.从session获取
#         # privkeystr = request.session.get('privkey').encode()
#         # 2.从文件获取，privkeystr为pcks#1格式，bytes
#         with open('private/my_private_rsa_key.pem', 'r') as f:
#             privkeystr = f.read().encode()
#             f.close()
#         # privkey 为私钥对象，由n，e等数字构成
#         privkey = RSA.importKey(privkeystr)
#         cipher = PKCS1_v1_5.new(privkey)
#         # 现将base64编码格式的password解码，然后解密，并用decode转成str
#         password = cipher.decrypt(base64.b64decode(password.encode()), 'error').decode()
#         # 至此，password解密成功，省略后面验证用户名和密码的代码了。
#
#     else:
#         # 伪随机数方式生成RSA公私钥对
#         random_generator = Random.new().read
#         rsa = RSA.generate(1024, random_generator)
#         rsa_private_key = rsa.exportKey()
#         rsa_public_key = rsa.publickey().exportKey()
#         # 1. 以session的方式存储私钥，PKCS1格式
#         # request.session['privkey'] = rsa_private_key.decode()
#         # 2. 存储到静态文件
#         with open('private/my_private_rsa_key.pem', 'w+') as f:
#             f.write(rsa_private_key.decode())
#             f.close()
#         return render(request, 'loginrsa.html', {'pub_key': rsa_public_key.decode()})
#
#
# def login_bug(request):
#     if request.POST:
#         uid = request.POST['uid']
#         password = request.POST['password']
#         select = "select * from app1_loginmodel as r where r.uid= '"+uid+"' and r.password='"+password+"'"
#         cursor = connection.cursor()
#         cursor.execute(select)
#         raw1 = cursor.fetchall()
#         if(len(raw1) == 0):
#             return HttpResponse('''<a  href="/login">用户名或密码错误，请重新登录！</a>''')
#         else:
#             rep = redirect('/home/')
#             rep.set_cookie("is_login", True)
#             rep.set_cookie("uid", raw1[0][0])
#             return rep
#     return render(request, "login.html")
#
# def logout(request):
#     rep = redirect('/home')
#     rep.delete_cookie("is_login")
#     return rep
#
#
# def register(request):
#     if request.POST:
#         uid = request.POST.get("uid")
#         cursor = connection.cursor()
#         cursor.execute("select * from app1_loginmodel where uid = %s", [uid, ])
#         raws = cursor.fetchall()
#         if(len(raws)==0):
#             password = request.POST.get("password")
#             # encrypt_password = make_password(password)
#             # cursor.execute("insert into app1_loginmodel values(%s,%s)", [uid, encrypt_password])
#             return HttpResponse('''<script>alert("注册成功，返回登录！");window.location.href="/login"</script>''')
#         else:
#             return HttpResponse('''<script>alert("该用户ID已注册！");window.location.href="/register"</script>''')
#     else:
#         return render(request, "register.html")