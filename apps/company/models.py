from django.db import models


class Desc(models.Model):
    """定义一个企业描述"""
    name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    company_url = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    desc = models.TextField()  # 简介
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)


class GongShang(models.Model):
    """定义一个工商信息"""
    name = models.CharField(max_length=255)
    faren = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    xn_href = models.CharField(max_length=255)


class HuaXiang(models.Model):
    """定义一个企业画像"""
    youshi = models.CharField(max_length=255)
    fenlei = models.CharField(max_length=255)
    biaoxian = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)


class Result(models.Model):
    """搜索结果页面"""
    title = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)
    highlight = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255)


class RongZi(models.Model):
    """融资历程"""
    lunci = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    money = models.CharField(max_length=255)
    zifang = models.CharField(max_length=255)
    bili = models.CharField(max_length=255)
    guzhi = models.CharField(max_length=255)
    fa = models.CharField(max_length=255)
    laiyuan = models.CharField(max_length=255)
    xn_href = models.CharField(max_length=255)
