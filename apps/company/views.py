import time
import os
import hmac
import hashlib
from hashlib import md5  # 导入md5加密
import datetime
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
from .models import Result, Desc, GongShang
from .data_deal import Desc_maker, GongShang_maker
import requests
from lxml import etree
import re
import json


def company_detail(request, xn_href):
    """公司详情 """
    # try:
    if 1==1:

        gs_info = GongShang.objects.filter(
            xn_href=xn_href).exists()
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
                # 企业描述
                Desc.objects.update_or_create(defaults={
                    "name": com_info["name"],
                    "xn_href": xn_href,
                    "brief": com_info["brief"],
                    "desc": com_info["desc"],
                    "roundName": com_info["roundName"],
                    "cityName": com_info["cityName"] + ">" + com_info["districtName"],
                    "establishDate": datetime.date.fromtimestamp(com_info["establishDate"] / 1000),
                    "img_url": com_info['logo'],
                    "company_url": com_info['website'],
                    "phone": contact_info.get("telephone", ""),
                    "email": contact_info.get("email", ""),
                    "address": contact_info.get("address", ""),
                }, xn_href=xn_href)
                # 工商信息写入
                gs_name = gongshang.get("name", "")
                # 法人
                legalPersonName = gongshang.get("legalPersonName", "")
                # 成立时间
                establishTime = gongshang.get("establishTime", "0")
                # 工商描述
                businessScope = gongshang.get("businessScope", "")
                # 经营状态
                regStatus = gongshang.get("regStatus", "")
                # 注册资本
                regCapital = gongshang.get("regCapital", "")

                print("======")
                # 融资历程

                licheng = cont["props"]["pageProps"]["fundings"]
                for licheng in cont["props"]["pageProps"]["fundings"]:
                    print(licheng)
                    roundName = licheng["roundName"]
                    fundingDate = licheng["fundingDate"]
                    fundingDesc = json.loads(licheng["fundingDesc"])
                    # 估值
                    postMoney = fundingDesc["postMoney"]
                    money = fundingDesc["money"]
                    # 比例
                    ratio = fundingDesc["ratio"]
                    # 投资方

                    if fundingDesc.get("investorStr", None) is None:
                        investorStr = ""
                    else:
                        investorArr = json.loads(fundingDesc["investorStr"])
                        in_arr = []
                        for item in investorArr:
                            in_arr.append(item['text'])
                        investorStr = "".join(in_arr)
                    print("investorStr====", investorStr)
                # # 工商信息
                # print(cont["props"]["pageProps"]["gongshang"])

                # print("======")
                # 标签画像

                # 优势
                # # 行业分类
                # print(cont["props"]["pageProps"]["tileTagList"])
                tileTagListArr = cont["props"]["pageProps"]["tileTagList"]
                tag_arr_hy = []
                tag_arr_ys = []
                for item in tileTagListArr:
                    if item['confidence']:
                        tag_arr_ys.append(item['name'])
                    else:
                        tag_arr_hy.append(item['name'])

                print("youshi", tag_arr_ys)
                print("hangye", tag_arr_hy)


        lang = request.GET.get("lang", "cn")
        context = {
            'news': result_info,
            'lang': lang
        }
        return render(request, 'company/hs_company_detail.html', context=context)
    # except Exception as e:
    #     raise Http404  # 抛出一个404错误，当抛出404时，django就会在根文件中的templates文件调用一个叫做404的文件
