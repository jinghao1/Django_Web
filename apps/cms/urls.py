from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import company_views
from . import staff_views

# from rest_framework import routers


app_name = 'cms'

# router = routers.DefaultRouter()
# router.register(path('',))

urlpatterns = [
    path('', views.index, name='index'),
    path('news_list/', views.NewsList.as_view(), name='news_list'),
    path('write_news/', views.WriteNewsView.as_view(), name='write_news'),
    path('edit_news/', views.EditNewsViem.as_view(), name='edit_news'),
    path('delete_news/', views.delete_news, name='delete_news'),
    path('news_category/', views.NewsCategoryViem.as_view(), name='news_category'),
    path('add_news_category/', views.add_news_category, name='add_news_category'),
    path('edit_news_category/', views.edit_news_category, name='edit_news_category'),
    path('delete_news_category/', views.delete_news_category, name='delete_news_category'),
    path('banners/', views.banners, name='banners'),
    path('banner_list/', views.banner_list, name='banner_list'),
    path('add_banner/', views.add_banner, name='add_banner'),
    path('delete_banner/', views.delete_banner, name='delete_banner'),
    path('edit_banner/', views.edit_banner, name='edit_banner'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('qntoken/', views.qntoken, name='qntoken'),

    path('news_show', views.NewsClickShowView.as_view(), name='news_show'),
]
#公司管理的url
urlpatterns += [
    path('company_list/', company_views.PubCompany.as_view(), name='company_list'),
    # path('course_category/', course_views.CourseCategoryViem.as_view(), name='course_category'),
    # path('add_course_category/', course_views.add_course_category, name='add_course_category'),
    # path('edit_course_category/', course_views.edit_course_category, name='edit_course_category'),
    # path('delete_course_category/', course_views.delete_course_category, name='delete_course_category'),
    # path('course_teacher/', course_views.CourseTeacher.as_view(), name='course_teacher'),
    # path('course_teacher/<pk>/', course_views.CourseTeacherDetail.as_view(), name='course_teacher_detail'),
    # path('course_teacher_list/', course_views.CourseTeacherList.as_view(), name='course_teacher_list'),
    # path('course_teacher_list/<pk>/', course_views.CourseTeacherListDetail.as_view(), name='course_teacher_list_detail'),
]

# # 分享资料urlwrite_news
# urlpatterns += [
#     path('pay_info/', views.PayInfoIndex.as_view(), name='pay_info'),
#     path('payinfo_list/', views.PayInfoList.as_view(), name='payinfo_list'),
#     path('payinfo/', views.PayInfo.as_view(), name="payinfo"),
#     path('payinfo/<pk>/', views.PayInfo.as_view(), name="payinfo_detail"),
# ]

# 用户管理相关url配置
urlpatterns += [
    path('staffs/', staff_views.staffs, name='staffs'),
    path('add_staff/', staff_views.AddStaffView.as_view(), name='add_staff'),
    path('delete_staff/', staff_views.DelStaffView.as_view(), name='del_staff'),
    path('user_center/', views.UserCenter.as_view(), name='user_center'),
    path('edit_user_center/', views.EditUserCenter.as_view(), name='edit_user_center'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
