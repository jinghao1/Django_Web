# encoding: utf-8
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.models import Group
from django.shortcuts import redirect, reverse
from apps.xfzauth.decorators import xfz_superuser_required
from django.utils.decorators import method_decorator
from django.contrib import messages
import logging
from apps.xfzauth.models import User
from utils import restful  # 引入自定义的浏览器返回的错误信息文件
logger = logging.getLogger("django")


@xfz_superuser_required
def staffs(request):
    """员工用户管理"""
    staffs = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True)).order_by("-id")
    context = {
        'staffs': staffs
    }
    return render(request, 'cms/staffs.html', context=context)


@method_decorator(xfz_superuser_required, name='dispatch')
class AddStaffView(View):
    """添加用户"""

    def get(self, request):
        # 获取Group表中的所有数据
        groups = Group.objects.all()
        pk = request.GET.get('pk')
        if pk:
            user_info = User.objects.filter(id=pk).first()
        else:
            user_info = {}

        context = {
            'groups': groups,
            "user_info": user_info
        }
        logger.info("user_info")
        logger.info(user_info.username)
        return render(request, 'cms/add_staff.html', context=context)

    def post(self, request):
        telephone = request.POST.get('telephone')
        is_superuser = request.POST.get('category', '0')

        if is_superuser == '0':
            is_superuser = False
        else:
            is_superuser = True
        # logger.info('添加文章分===类:%s！' % is_superuser)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = User.objects.filter(telephone=telephone).first()
        if not user:

            user = User.objects.create_superuser(
                telephone=telephone, username=username, password=password, is_staff=1, is_superuser=is_superuser)


        else:
            User.objects.filter(telephone=telephone).update(
                telephone=telephone, username=username, password=password, is_staff=1, is_superuser=is_superuser)
        return redirect(reverse("cms:staffs"))  # 重定向到员工管理界面


@method_decorator(xfz_superuser_required, name='dispatch')
class DelStaffView(View):

    def post(self, request):
        pk = request.POST.get('pk')
        try:
            User.objects.filter(pk=pk).delete()
            return restful.ok()
        except BaseException as e:
            logger.error(e)
            return restful.params_error(message='该用户不存在！')
