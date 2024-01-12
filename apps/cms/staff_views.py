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

logger = logging.getLogger("django")


@xfz_superuser_required
def staffs(request):
    """员工用户管理"""
    staffs = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
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
        context = {
            'groups': groups
        }
        return render(request, 'cms/add_staff.html', context=context)

    def post(self, request):
        telephone = request.POST.get('telephone')
        is_staff = request.POST.get('category', '0')
        logger.info('添加文章分类:%s！' % is_staff)
        if is_staff == '0':
            is_superuser = False
        else:
            is_superuser = True
        logger.info('添加文章分===类:%s！' % is_superuser)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = User.objects.filter(telephone=telephone)
        if not user:

            user = User.objects.create_superuser(
                telephone=telephone, username=username, password=password, is_staff=1, is_superuser=is_superuser)
            return redirect(reverse("cms:staffs"))  # 重定向到员工管理界面
            # return restful.ok()
            # 这里不能使用get请求，因为get请求只能获取一个参数，
            # 但是这里是需要获取多个参数，所以使用getlist
            groups_ids = request.POST.getlist('groups')

            groups = Group.objects.filter(pk__in=groups_ids)  # 获取所有筛选的分组
            # 建立一个分组
            # print('groups_ids:%s'%groups_ids)
            # print('groups:%s'%groups)
            user.groups.set(groups)
            user.save()
            return redirect(reverse("cms:staffs"))  # 重定向到员工管理界面
        else:
            messages.info(request, "用户已存在，请检查输入信息是否有误！")
            return redirect(reverse("cms:add_staff"))


def delete_staff():
    """删除员工"""
    pass
