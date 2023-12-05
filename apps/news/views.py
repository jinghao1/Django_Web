from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings
from django.http import Http404
# 当我们在查询的条件中需要组合条件时(例如两个条件“且”或者“或”)时。
# 我们可以使用Q()查询对象
from django.db.models import Q
# from silk.profiling.profiler import silk_profile
from django.http import JsonResponse
# login_required：只能针对传统的页面跳转（如果没有登录，就跳转到login_url指定的页面）
# 但是他不能处理这种ajax请求。就是说如果通过ajax请求去访问一个需要授权的页面
# 那么这个装饰器的页面跳转功能就不行了,针对Ajax请求的页面跳转自定义一个装饰器
# from django.contrib.auth.decorators import login_required
from apps.xfzauth.decorators import xfz_login_required  # y导入自定义的用于ajax请求的装饰器
from .serializers import NewsSerializer, CommentSerializer  # 导入定义序列化
from utils import restful
from .forms import AddCommentForm
from .models import Comment
from .models import NewCategory, News, Banner
import requests
import re
import copy
# from bs4 import BeautifulSoup


# @silk_profile(name='get_news')
def index(request):
    """新闻显示页,加入轮播图"""
    # newses = News.objects.all()
    # 用于加载界面显示新闻的个数，settings中设置的ONE_PAGE_NEWS_COUNT是1，
    # 这里配置后，界面只会展示1篇文章
    newses = News.objects.select_related('category', 'author')[
             0:settings.ONE_PAGE_NEWS_COUNT]
    categories = NewCategory.objects.all()
    banners = Banner.objects.all()  # 获取轮播图
    # context 中''中的数据是传入HTML模板中的变量，
    # print(type(banners), 'banners:%s' % banners)
    context = {
        'newses': newses,
        'categories': categories,
        'banners': banners  # 将轮播图数据返回给前端
    }
    return render(request, 'news/index.html', context=context)


# hs cn index
def hs_cn_index(request):
    search_string = request.GET.get("s_search", None)
    lang = request.GET.get("lang", "cn")
    if search_string is None:
        # title = models.CharField(max_length=200)  # 题目
        # desc = models.CharField(max_length=200)  # 描述
        # thumbnail = models.URLField()  # 缩略图链接
        # content = models.TextField()  # 发布内容
        # pub_time = models.DateTimeField(auto_now=True)  # 发布时间，设置为当前时间
        newses = News.objects.select_related('category', 'author')[
                 0:settings.ONE_PAGE_NEWS_COUNT]
        # categories = NewCategory.objects.all()
        # banners = Banner.objects.all()  # 获取轮播图
        # context 中''中的数据是传入HTML模板中的变量，
        # print(type(banners), 'banners:%s' % banners)
        for item in newses:
            print(item.content)
            en_con = copy.deepcopy(item.content)
            result = re.findall(r'[\u4e00-\u9fa5]+', item.content)
            line_inde = 0
            for line_one in result:
                line_inde += 1
                print(line_one)
                if line_inde >9:
                    break
            print("end++++")
            break

        if lang == "en":
            menu_about_name = "ABOUT US"
            menu_data_name = "DATA"
        else:
            menu_about_name = "关于我们"
            menu_data_name = "数据仓库"
        context = {
            'newses': newses,
            'smalles': [2, 3, 6, 7],
            'lang': lang,
            'menu_about_name': menu_about_name,
            'menu_data_name': menu_data_name,
            # 'categories': categories
            # 'banners': banners  # 将轮播图数据返回给前端
        }
        if lang == "en":
            return render(request, 'hs/index_en.html', context=context)
        else:
            return render(request, 'hs/index.html', context=context)
    else:
        # try:
        #     headers = {
        #         "Referer": "/team/?s_page=1&s_per_page=6&s_search=字节&s_subtype=founder%2Ccompany%2Cteam-member%2Cpost"
        #     }
        #     result = requests.get(url, headers=headers, timeout=6)
        #     print(result)
        # except Exception as e:
        if 1 == 1:
            result = {
                "results": [
                    {
                        "ID": 525,
                        "post_title": "\u7ea2\u6749X\u98de\u4e66\u300c\u7ec4\u7ec7\u8fdb\u5316\u8bba\u300d\uff1a\u4e3a\u4ec0\u4e48\u5148\u8fdb\u7ec4\u7ec7\u53ef\u4ee5\u4fdd\u6301\u5f39\u6027\uff1f| Human Capital Talk\u7b2c\u56db\u671f",
                        "post_type": "post",
                        "permalink": "\/article\/sequoia-feishu-human-capital-talk-4\/",
                        "terms": [],
                        "meta": [],
                        "acf": {
                            "post_author_profile": null
                        }
                    },
                    {
                        "ID": 986,
                        "post_title": "\u5b57\u8282\u8df3\u52a8",
                        "post_type": "company",
                        "permalink": "\/companies\/bytedance\/",
                        "terms": {
                            "sector": [
                                {
                                    "term_id": 12,
                                    "slug": "tech",
                                    "name": "\u79d1\u6280",
                                    "parent": 0,
                                    "term_taxonomy_id": 12,
                                    "term_order": 0,
                                    "facet": "{\"term_id\":12,\"slug\":\"tech\",\"name\":\"\\u79d1\\u6280\",\"parent\":0,\"term_taxonomy_id\":12,\"term_order\":0}"
                                }
                            ]
                        },
                        "meta": []
                    }
                ],
                "total": 2,
                "totals": {
                    "post": 1,
                    "company": 1
                }
            }

        return JsonResponse(result)


# 关于我们
def hs_cn_about_us(request):
    newses = News.objects.select_related('category', 'author')[
             0:settings.ONE_PAGE_NEWS_COUNT]
    categories = NewCategory.objects.all()
    banners = Banner.objects.all()  # 获取轮播图
    lang = request.GET.get("lang", "cn")
    # context 中''中的数据是传入HTML模板中的变量，
    # print(type(banners), 'banners:%s' % banners)
    context = {
        'newses': newses,
        'categories': categories,
        'lang': lang,
        'banners': banners  # 将轮播图数据返回给前端
    }
    return render(request, 'hs/about_us.html', context=context)


# 搜索
def hs_cn_search(request):
    newses = News.objects.select_related('category', 'author')[
             0:settings.ONE_PAGE_NEWS_COUNT]
    categories = NewCategory.objects.all()
    banners = Banner.objects.all()  # 获取轮播图
    # context 中''中的数据是传入HTML模板中的变量，
    # print(type(banners), 'banners:%s' % banners)
    context = {
        'newses': newses,
        'categories': categories,
        'banners': banners  # 将轮播图数据返回给前端
    }
    return render(request, 'hs/search_cn.html', context=context)


@require_GET
def news_list(request):
    """
    新闻列表,用于当加载更多时，翻页
    """
    # /news/list/?p=3
    # 对于没有捕获的p参数，我们后面加一个默认参数，避免浏览器获取数据类型错误
    page = int(request.GET.get('p', 1))
    # 分类的id就叫做"category_id"
    category_id = int(request.GET.get('category_id', 0))  # 获取分类id
    # offer,limit
    start = settings.ONE_PAGE_NEWS_COUNT * (page - 1)
    end = start + settings.ONE_PAGE_NEWS_COUNT
    # newses：QuerySet -> [News(),News()] 下面的值
    # newses对象： [{"title":"","content":''},{"title":"","content":''}]
    # newses = list(News.objects.all()[start:end].values())
    # value:将QuerySet中的模型对象（比如News()对象）转换为字典
    # 加list直接强制将QuerySet转换为列表

    # 当定义好Newserializers并引入后，就可以直接使用***serializer定义
    if category_id == 0:
        # 如果category_id等于0，说明用户未创建分类
        newses = News.objects.all()[start:end]
    else:
        newses = News.objects.filter(category_id=category_id)[start: end]
    serializer = NewsSerializer(newses, many=True)
    return restful.result(data=serializer.data)


def news_detail(request, news_id):
    """新闻详情 """
    try:
        news = News.objects.select_related(
            'category', 'author').get(
            pk=news_id)
        lang = request.GET.get("lang", "cn")
        context = {
            'news': news,
            'lang': lang
        }
        return render(request, 'news/hs_news_detail.html', context=context)
    except News.DoesNotExist:
        raise Http404  # 抛出一个404错误，当抛出404时，django就会在根文件中的templates文件调用一个叫做404的文件


@require_POST
@xfz_login_required
def add_comment(request):
    """评论"""
    # 对于django种如果没有登录用户，也还是会有一个request.user ->AnonymousUser的一个假用户，
    # 这个用户数据是不能存储在数据库的
    form = AddCommentForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data.get('content')
        news_id = form.cleaned_data.get('news_id')
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(
            content=content, news=news, author=request.user)  # 创建评论
        serizlize = CommentSerializer(comment)
        return restful.result(data=serizlize.data)  # 获取数据
    else:
        return restful.params_error(message=form.get_error())


def search(request):
    """查询，返回一个查询页面 """
    q = request.GET.get('q')

    # 限制字符串长度超过20
    if len(str(q)) < 20:
        if q:
            # 搜索对象为：title或者content中包含的关键字，有就返回
            newes = News.objects.filter(
                Q(title__icontains=q) | Q(content__icontains=q))
            if newes:
                flag = 2
            else:
                page = int(request.GET.get('p', 1))
                start = settings.ONE_PAGE_NEWS_COUNT * (page - 1)
                end = start + settings.ONE_PAGE_NEWS_COUNT
                newes = News.objects.all()[start:end]
                flag = 1
        else:
            page = int(request.GET.get('p', 1))
            start = settings.ONE_PAGE_NEWS_COUNT * (page - 1)
            end = start + settings.ONE_PAGE_NEWS_COUNT
            newes = News.objects.all()[start:end]
            flag = 0

        context = {'newes': newes, 'flag': flag}
        return render(request, 'news/search.html', context=context)
    else:
        flag = 3
        context = {'flag': flag}
        return render(request, 'news/search.html', context=context)
