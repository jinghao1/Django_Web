import logging

from django.views.generic import View  # 使用类方法定义视图函数引入的View模块
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.xfzauth.decorators import xfz_permission_required
# from apps.course.serializers import TeacherSerializers
# from apps.course.models import CourseCategory, Teacher, Course
from apps.company.models import Desc,GongShang
from .forms import AddCourseForm, EditCoursesCategoryForm  # 导入需要的form表单
from utils import restful  # 导入返回信息判断文件

# restful表格处理
# from django.shortcuts import get_object_or_404, redirect
# from apps.course.models import Teacher
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework.response import Response


logger = logging.getLogger("django")  # 初始化logger模块


# @method_decorator(login_required, name='dispatch')
class PubCompany(View):
    """公司信息列表"""

    def get(self, request):
        page = int(request.GET.get('p', 1))  # 获取当前所在页数
        start = request.GET.get('start')   # 通过前端的标签名获取值
        end = request.GET.get('end')
        title = request.GET.get('title')
        category_id = int(request.GET.get('category', 0))

        # newses = News.objects.select_related ('category', 'author').all () #
        # 获取所有新闻分类及作者
        companyes = GongShang.objects.all()

     

        # 过滤标题中包含指定关键字的新闻
        if title:
            newses = companyes.filter(
                title__icontains=title)  # i指忽略大小写，contains指包含

        # 过滤对应分类的新闻
        if category_id != 0:
            newses = newses.filter(category=category_id)
            # print('分类名称：%s' % category_id, '新闻数量%s' % len(newses))
        paginator = Paginator(newses, 10)  # 将获取的新闻内容按照每页2篇的形式进行分页
        page_obj = paginator.page(page)  # 获取对应分页的数据
        categories = NewCategory.objects.all()

        # 通过分页函数返回分页数据，获取每一页的数据
        pagination_data = self.get_pagination_data(paginator, page_obj)
        '''查询内容组成的查询url是否应该带'''
        # 方法1：
        # if (start and end) or title or category_id!=0 :
        # 	url_query = '&' + parse.urlencode ({
        # 		'start': start,
        # 		'end': end,
        # 		'title': title,
        # 		'category': category_id
        # 	})
        # else:
        # 	url_query = ''
        # 方法2：
        if start or end or title or category_id:
            url_query = '&' + parse.urlencode({
                'start': start,
                'end': end,
                'title': title,
                'category': category_id
            })
        else:
            url_query = ''

        context = {
            'categories': categories,
            'paginator': paginator,
            'page_obj': page_obj,
            'newses': page_obj.object_list,  # 获取该页数据的内容
            'title': title,
            'start': start,
            'end': end,
            'category_id': category_id,
            # 查询内容url
            'url_query': url_query
        }
        logger.info('用户查询了[%s]' % context['url_query'])
        # print(context['url_query'])  # 打印测试输出的是否是我们查询内容
        context.update(pagination_data)
        return render(request, 'cms/news_list.html', context=context)
        return render(request, 'cms/company_list.html', context=context)

    def post(self, request):
        form = AddCourseForm(request.POST)
        if form.is_valid():
            # 从form表单中获取数据赋值给model中定义的变量
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            teacher_id = form.cleaned_data.get('teacher_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get('cover_url')
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            # 从form表单中获取的id数据,通过对应模型获取到category和teacher的具体值
            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)

            # 将以上整理的数据写入数据库的Course模型
            Course.objects.create(
                title=title,
                category=category,
                teacher=teacher,
                video_url=video_url,
                cover_url=cover_url,
                price=price,
                duration=duration,
                profile=profile
            )
            return restful.ok()
        else:
            return restful.params_error(form.get_error())
