from django.urls import path
from . import views
# from django.shortcuts import reverse


# 设置空间名
app_name = 'company'
urlpatterns = [
	path('company/<xn_href>/overview', views.company_detail, name='company_detail'),
]
