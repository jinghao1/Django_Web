import time
import os
import hmac
import hashlib
from hashlib import md5  # 导入md5加密
import datetime
from datetime import timedelta
from django.forms.models import model_to_dict

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import reverse  # 重定向模块
from django.views.decorators.csrf import csrf_exempt  # 导入装饰器
from django.shortcuts import redirect
from apps.xfzauth.decorators import xfz_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required  # 导入登录验证函数
from django.utils.decorators import method_decorator  # 验证登录才能访问函数的装饰器
from utils.xn_request import xn_company_detail
from utils import restful
from .models import Result, Desc, GongShang, RongZi, HuaXiang
from .data_deal import Desc_maker, GongShang_maker
import requests
from lxml import etree
import re
import json


def company_detail(request, xn_href):
    """公司详情 """
    # try:
    if 1 == 1:
        result_info = {}
        dt_s = datetime.datetime.now().date()  # 2018-7-15
        dt_e = (dt_s - timedelta(7))  # 2018-7-08
        # print(dt_e)
        #objs = Record.objects.filter(end_time__range=[dt_s, dt_e])
        #objs = Record.objects.filter(Q(end_time__=dt_s) & Q(end_time__lt=dt_e))  # 效果相同
        gs_info = GongShang.objects.filter(
            xn_href=xn_href,date__gt=dt_e).exists()
        # print("gs_info",gs_info)
        if not gs_info:
            response = xn_company_detail(xn_href)
            if "status_code" in dir(response) and response.status_code == 200:
                # 获取页面资源
                page_text = response.text
                # scriptlis = re.findall(r'<script>(.*?)</script>', page_text)
                content = re.findall(r'__NEXT_DATA__ = (.*?);__NEXT_LOADED_PAGES__=', page_text)
                cont = json.loads(content[0])
                # company desc
                com_info = cont["props"]["pageProps"]["company"]
                gongshang = json.loads(cont["props"]["pageProps"]["gongshang"])
                # 联系方式
                contact_info = gongshang.get("contact", {})
                if not com_info.get("districtName",""):
                    cityName = com_info.get("cityName","")
                else:
                    cityName = com_info.get("cityName", "") + ">" + str(com_info.get("districtName", ""))
                # 企业描述
                Desc.objects.update_or_create(defaults={
                    "name": com_info["name"],
                    "xn_href": xn_href,
                    "brief": com_info["brief"],
                    "desc": com_info["desc"],
                    "roundName": com_info.get("roundName",""),
                    "cityName": cityName,
                    "establishDate": datetime.date.fromtimestamp(com_info["establishDate"] / 1000),
                    "img_url": com_info['logo'],
                    "company_url": com_info['website'],
                    "phone": contact_info.get("telephone", ""),
                    "email": contact_info.get("email", ""),
                    "address": contact_info.get("address", ""),
                }, xn_href=xn_href)
                # 工商信息写入
                GongShang.objects.update_or_create(
                    defaults={
                        "code": com_info["code"],
                        "xn_href": xn_href,
                        "fullName": com_info["fullName"],
                        "legalPersonName": gongshang["legalPersonName"],  # 法人
                        "establishTime": datetime.date.fromtimestamp(gongshang.get("establishTime", 0) / 1000),  # 成立时间
                        "businessScope": gongshang['businessScope'],  # 工商描述
                        "regCapital": gongshang.get("regCapital", ""),  # 注册资本
                        "regStatus": gongshang.get("regStatus", ""),  # 经营状态
                        "date": datetime.date.fromtimestamp(time.time()),
                    }, xn_href=xn_href
                )
                # 融资历程
                # print("rongzi......")
                licheng = cont["props"]["pageProps"]["fundings"]
                for licheng in cont["props"]["pageProps"]["fundings"]:
                    fundingDesc = json.loads(licheng["fundingDesc"])
                    xn_id = str(licheng.get("id", "1"))
                    if fundingDesc.get("investorStr", None) is None:
                        investorStr = ""
                    else:
                        investorArr = json.loads(fundingDesc["investorStr"])
                        in_arr = []
                        for item in investorArr:
                            in_arr.append(item['text'])
                        investorStr = "".join(in_arr)
                    RongZi.objects.update_or_create(
                        defaults={
                            "xn_href": xn_href,
                            "xn_id": xn_id,  # 犀牛id
                            "roundName": licheng["roundName"],
                            "fundingDate": datetime.date.fromtimestamp(licheng.get("fundingDate", 0) / 1000),
                            "postMoney": fundingDesc.get("postMoney",""),  # 估值
                            "money": fundingDesc.get("money", ""),  # 投资金额
                            "ratio": fundingDesc.get("ratio", ""),  # 投资比例
                            "newsLink": licheng.get("newsLink", ""),  # 犀牛新闻链接
                            "investorStr": investorStr,  # 投资方
                            "date": datetime.date.fromtimestamp(time.time()),  # 录入时间
                        }, xn_href=xn_href, xn_id=xn_id
                    )
                    # 标签画像 优势 行业分类
                tileTagListArr = cont["props"]["pageProps"]["tileTagList"]
                tag_arr_hy = []
                tag_arr_ys = []
                for item in tileTagListArr:
                    if item['confidence']:
                        tag_arr_ys.append(item['name'])
                    else:
                        tag_arr_hy.append(item['name'])
                HuaXiang.objects.update_or_create(
                    defaults={
                        "xn_href": xn_href,
                        "youshi": " ".join(tag_arr_ys),  # 优势
                        "fenlei": " ".join(tag_arr_hy),  # 行业
                        "date": datetime.date.fromtimestamp(time.time()),  # 录入时间
                    }, xn_href=xn_href
                )

        gs_info = GongShang.objects.filter(
            xn_href=xn_href).first()
        desc_info = Desc.objects.filter(
            xn_href=xn_href).first()

        hx_info = HuaXiang.objects.filter(
            xn_href=xn_href).first()
        if hx_info:
            if hx_info.youshi:
                hx_info.youshi = hx_info.youshi.split(" ")
            if hx_info.fenlei:
                hx_info.fenlei = hx_info.fenlei.split(" ")
        rz_info = RongZi.objects.filter(
            xn_href=xn_href).all()
        rz_arr = []
        if rz_info:
            for item in rz_info:
                rz_arr.append(model_to_dict(item))

        # print(result_info)
        lang = request.GET.get("lang", "cn")
        context = {
            'rz_arr': rz_arr,
            'gs_info': gs_info,
            'desc_info': desc_info,
            'hx_info': hx_info,
            'lang': lang
        }
        return render(request, 'xn/xn_detail.html', context=context)
        # return render(request, 'company/hs_company_detail.html', context=context)
    # except Exception as e:
    #     raise Http404  # 抛出一个404错误，当抛出404时，django就会在根文件中的templates文件调用一个叫做404的文件
