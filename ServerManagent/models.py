from django.db import models
from django.utils.html import format_html
# Create your models here.

class ServerManagent(models.Model):
    classnum = models.CharField(max_length=5)
    provider = models.CharField(max_length=5)
    service = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=10)
    system = models.CharField(max_length=15)
    outside = models.CharField(max_length=15)
    inside = models.CharField(max_length=15)
    cpu = models.CharField(max_length=55)
    memory = models.CharField(max_length=3)
    disk = models.CharField(max_length=10)
    date = models.DateField()
    status_choices = (('ON',u"运行"),
                      ('stopping', u"准备停"),
                      ('stoped', u"已停"),
                      ('free', u"免费")
                      )
    status = models.CharField(choices=status_choices, max_length=10, default="ON")

    def __str__(self):
        return self.name

    def colored_status(self):

        if self.status == "ON":
            color_code = 'green'
            format_td = format_html('<span style=color:{};">{}</span>',color_code,"运行")
        elif self.status == "stopping":
            color_code = 'SandyBrown'
            format_td = format_html('<span style=color:{};">{}</span>', color_code, "即将停用")
        elif self.status == "stoped":
            color_code = 'red'
            format_td = format_html('<span style=color:{};">{}</span>', color_code, "已停用")
        elif self.status == "free":
            color_code = 'blue'
            format_td = format_html('<span style=color:{};">{}</span>', color_code, "免费")

        return format_td

class AccountManagent(models.Model):
    category = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=55)
    style = models.CharField(max_length=10)
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class DBAccount(models.Model):
    category = models.CharField(max_length=5)
    style = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    address1 = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60)
    address3 = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class InsideName(models.Model):
    ip = models.CharField(max_length=15)
    mac = models.CharField(max_length=17)
    cpu = models.CharField(max_length=60)
    mem = models.CharField(max_length=3)
    disk = models.CharField(max_length=5)
    system = models.CharField(max_length=20)
    user = models.CharField(max_length=9)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.ip

class MailManagent(models.Model):
    name = models.CharField(max_length=10)
    account = models.CharField(max_length=35)
    password= models.CharField(max_length=15)
    def __str__(self):
        return self.name


