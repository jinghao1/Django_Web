import time
import os
import hmac
import hashlib
from hashlib import md5  # 导入md5加密

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import reverse  # 重定向模块
from django.views.decorators.csrf import csrf_exempt  # 导入装饰器
from django.shortcuts import redirect
from apps.xfzauth.decorators import xfz_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required  # 导入登录验证函数
from django.utils.decorators import method_decorator  # 验证登录才能访问函数的装饰器

from utils import restful
from .models import Result


def Result_maker(result_info):


    info = Result.objects.filter(
        xn_href=result_info['xn_href']).exists()
    if info:
        Result.objects.filter(xn_href=result_info['xn_href']).update(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            search_name=result_info['search_name'],
        )
        return "update"
    else:
        res = Result.objects.create(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            xn_href=result_info['xn_href'],
            search_name=result_info['search_name'],
        )
        return "insert"

    #
    # return restful.result(data={'result_id': res.id})


def company_detail(request, xn_href):
    """公司详情 """
    try:
        result_info = Result.objects.filter(
            xn_href=xn_href).first()
        lang = request.GET.get("lang", "cn")
        context = {
            'news': result_info,
            'lang': lang
        }
        return render(request, 'company/hs_company_detail.html', context=context)
    except News.DoesNotExist:
        raise Http404  # 抛出一个404错误，当抛出404时，django就会在根文件中的templates文件调用一个叫做404的文件
