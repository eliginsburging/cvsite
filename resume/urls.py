from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('quote/<author>', views.quote_detail, name='quote_api_author'),
    path('semester-list/', views.semester_list, name='semester-list'),
    path('semester/<pk>', views.semester_detail, name='semester-detail'),
    path('course/<pk>', views.course_detail, name='course-detail'),
    path('award/<pk>', views.award_detail, name='academicaward-detail'),
    path('award-list', views.award_list, name='academicaward-list'),
    path('apcourse/<pk>', views.apcourse_detail, name='apcourse-detail'),
    path('apcourse-list', views.apcourse_list, name='apcourse-list'),
    path('language/<pk>', views.language_detail, name='language-detail'),
    path('language-list/<iscurrent>', views.language_list, name='language-list'),
    path('language-det/<pk>', views.languagedetail_detail,
         name='languagedetail-detail'),
]
