from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('quote/<author>', views.quote_detail, name='quote_api_author')
]
