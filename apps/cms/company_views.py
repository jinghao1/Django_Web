import logging
from urllib import parse  # 导入url函数
from django.views.generic import View  # 使用类方法定义视图函数引入的View模块
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator  # django自带分页处理
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


@method_decorator(login_required, name='dispatch')
class PubCompany(View):
    """公司信息列表"""
    def get_pagination_data(self, paginator, page_obj, around_count=1):
        """
        分页功能
        < 1...5,6,7,8,9...13 >基本模式，即选中页前后留出2页，多出的用...代替。
        当选择最前或最后前后两页包含或者临近第一页或最后一页，那么取消显示...
        """
        current_page = page_obj.number  # 获取当前页码
        num_pages = paginator.num_pages

        # 左侧是否应该显示三个点
        left_has_more = False

        # 右侧是否应该显示三个点
        right_has_more = False

        # 左侧显示页
        # 判断当前页数小于需要展示页数+2时，不显示三个点
        l_start = current_page - around_count  # 左侧的开始页码数
        l_end = current_page  # 右侧结束页码数
        if current_page <= around_count + 2:
            left_pages = range(1, l_end)
        else:
            left_has_more = True
            left_pages = range(l_start, l_end)

        # 右侧显示页
        r_start = current_page + 1
        r_end = current_page + around_count + 1   # ? 说绝对位置是是这个位置+1?
        if current_page >= num_pages - around_count - 1:
            right_pages = range(r_start, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(r_start, r_end)
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages,
            'current_page': current_page
        }
    def get(self, request):
        page = int(request.GET.get('p', 1))  # 获取当前所在页数 
        title = request.GET.get('title') 
        # newses = News.objects.select_related ('category', 'author').all () #
        # 获取所有新闻分类及作者
        companyes = GongShang.objects.all().order_by("-id")

        # 过滤标题中包含指定关键字的新闻
        if title:
            companyes = companyes.filter(
                fullName__icontains=title)  # i指忽略大小写，contains指包含

 
        paginator = Paginator(companyes, 10)  # 将获取的新闻内容按照每页2篇的形式进行分页
        page_obj = paginator.page(page)  # 获取对应分页的数据
   

        # 通过分页函数返回分页数据，获取每一页的数据
        pagination_data = self.get_pagination_data(paginator, page_obj)
        '''查询内容组成的查询url是否应该带'''
     
        # 方法2：
        if   title:
            url_query = '&' + parse.urlencode({
      
                'title': title
       
            })
        else:
            url_query = ''

        context = {
 
            'paginator': paginator,
            'page_obj': page_obj,
            'comes': page_obj.object_list,  # 获取该页数据的内容
            'title': title, 
    
            # 查询内容url
            'url_query': url_query
        }
        logger.info('用户查询了[%s]' % context['url_query'])
        # print(context['url_query'])  # 打印测试输出的是否是我们查询内容
        context.update(pagination_data)
        # return render(request, 'cms/news_list.html', context=context)
        return render(request, 'cms/company_list.html', context=context)
 

@method_decorator(login_required, name='dispatch')
class EditPubCompany(View):
    def get(self, request):
        pk = request.GET.get('pk')
        lang = request.GET.get('lang',"cn") 
        gs_info = GongShang.objects.get(pk=pk)
        desc_info = Desc.objects.get(xn_href=gs_info.code)
   
        context = {
            'gs_info': gs_info,
            'desc_info': desc_info
        }
        if lang == "en":
            return render(request, 'cms/company_edit_en.html', context=context)
        else:
            return render(request, 'cms/company_edit.html', context=context)
 
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