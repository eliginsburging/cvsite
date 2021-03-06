from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.index_page,
         name='index'),
    path('quote/<author>',
         views.quote_detail,
         name='quote_api_author'),
    path('semester-list/',
         views.semester_list,
         name='semester-list'),
    path('semester/<pk>',
         views.semester_detail,
         name='semester-detail'),
    path('course/<pk>',
         views.course_detail,
         name='course-detail'),
    path('award/<pk>',
         views.award_detail,
         name='academicaward-detail'),
    path('award-list',
         views.award_list,
         name='academicaward-list'),
    path('apcourse/<pk>',
         views.apcourse_detail,
         name='apcourse-detail'),
    path('apcourse-list',
         views.apcourse_list,
         name='apcourse-list'),
    path('language/<pk>',
         views.language_detail,
         name='language-detail'),
    path('language-list/<iscurrent>',
         views.language_list,
         name='language-list'),
    path('language-det/<pk>',
         views.languagedetail_detail,
         name='languagedetail-detail'),
    path('skill/<pk>',
         views.skill_detail,
         name='skill-detail'),
    path('skill-list/',
         views.skill_list,
         name="skill-list"),
    path('skill-det/<pk>',
         views.skilldetail_detail,
         name='skilldetail-detail'),
    path('position-list',
         views.position_list,
         name='position-list'),
    path('position-det/<pk>',
         views.position_detail,
         name="position-detail"),
    path('priortitle-det/<pk>',
        views.priortitle_detail,
        name='priortitle-detail'),
    path('duty-det/<pk>',
         views.duty_detail,
         name="duty-detail"),
    path('dutytag-det/<pk>',
         views.dutytag_detail,
         name='dutytag-detail'),
    path('project-det/<pk>',
         views.project_detail,
         name='project-detail'),
    path('projecttag-det/<pk>',
         views.projecttag_detail,
         name='projecttag-detail')
]
