from django.urls import path
from . import views
# from django.shortcuts import reverse


# 设置空间名
app_name = 'news'
urlpatterns = [
	path('before', views.index, name='index'),
	path('', views.hs_cn_index, name='hongshan_index'),
	path('hs/cn_about_us', views.hs_cn_about_us, name='hs_about_us_cn'),
	path('hs/cn_search', views.hs_cn_search, name='hs_about_us_cn'),
	path('detail/<news_id>/', views.news_detail, name='news_detail'),
	path('search/', views.search, name='search'),
	path('list/', views.news_list, name='news_list'),
	path('add_comment/', views.add_comment, name='add_comment'),
]
