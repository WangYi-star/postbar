from django.db import models

# Create your models here.

class LoginModel(models.Model):
    uid = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=128)
    identity = models.CharField(max_length=32, null=True)

class PostModel(models.Model):
    postid = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=255)
    uid = models.CharField(max_length=64)
    # uid = models.ForeignKey("LoginModel", on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    posttime = models.CharField(max_length=32)
    recent = models.IntegerField()
    number = models.IntegerField()
    text = models.CharField(max_length=255, null=True)

class ReplyModel(models.Model):
    replyid = models.IntegerField(primary_key=True)
    postid = models.IntegerField()
    uid = models.CharField(max_length=64)
    # postid = models.ForeignKey("PostModel", on_delete=models.CASCADE)
    # uid = models.ForeignKey("LoginModel", on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    time = models.CharField(max_length=32)
    delete = models.IntegerField()
    order = models.IntegerField()
    content = models.CharField(max_length=255)

class UserModel(models.Model):
    uid = models.CharField(max_length=64, primary_key=True)
    # uid = models.ForeignKey("LoginModel", primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=64, null=True)
    intime = models.CharField(max_length=64, null=True)
    gender = models.CharField(max_length=4, null=True)
    birthday = models.CharField(max_length=32, null=True)
    sign = models.CharField(max_length=64, null=True)
    occupation = models.CharField(max_length=32, null=True)
    edress = models.CharField(max_length=32, null=True)
    phone = models.CharField(max_length=32, null=True)
    location = models.CharField(max_length=32, null=True)
    userintro = models.CharField(max_length=64, null=True)
    filename = models.CharField(max_length=64, null=True)