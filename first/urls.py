from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),
    # re_path(r'^select/(?P<year>[0-9]{4}/$)'), #정규표현식
    # path('select/<int:year>/', views)
    path('sum/', views.sum, name="sum"),
]