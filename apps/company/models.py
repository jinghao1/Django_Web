from django.db import models


class Desc(models.Model):
    """定义一个企业描述"""
    name = models.CharField(max_length=255)
    roundName = models.CharField(max_length=255)
    cityName = models.CharField(max_length=255,default="NUll",null=True)
    establishDate = models.DateTimeField()
    img_url = models.CharField(max_length=255)
    company_url = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)
    desc = models.TextField()  # 简介
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)


class GongShang(models.Model):
    """定义一个工商信息"""
    code = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    legalPersonName = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    establishTime = models.DateTimeField(auto_now_add=True)
    xn_href = models.CharField(max_length=255)
    businessScope = models.TextField()
    regCapital = models.CharField(max_length=255)
    regStatus = models.CharField(max_length=255)


class HuaXiang(models.Model):
    """定义一个企业画像"""
    youshi = models.CharField(max_length=255)
    fenlei = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    xn_href = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Result(models.Model):
    """搜索结果页面"""
    title = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)
    highlight = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255)


class RongZi(models.Model):
    """融资历程"""
    xn_href = models.CharField(max_length=255)
    xn_id = models.CharField(max_length=50)
    roundName = models.CharField(max_length=255)
    postMoney = models.CharField(max_length=255)
    money = models.CharField(max_length=255)
    ratio = models.CharField(max_length=255,default="NUll",null=True)
    newsLink = models.CharField(max_length=255)
    investorStr = models.CharField(max_length=255)
    fundingDate = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)

