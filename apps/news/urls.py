from django.urls import path
from . import views
# from django.shortcuts import reverse


# 设置空间名
app_name = 'news'
urlpatterns = [
	path('', views.index, name='index'),
	path('hs/cn', views.hs_cn_index, name='hongshan_index'),
	path('detail/<news_id>/', views.news_detail, name='news_detail'),
	path('search/', views.search, name='search'),
	path('list/', views.news_list, name='news_list'),
	path('add_comment/', views.add_comment, name='add_comment'),
]
