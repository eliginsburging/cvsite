from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('quote/<author>', views.quote_detail, name='quote_api_author'),
    path('semester-list/', views.semester_list, name='semester-list'),
    path('semester/<pk>', views.semester_detail, name='semester-detail'),
    path('course/<pk>', views.course_detail, name='course-detail')
]
