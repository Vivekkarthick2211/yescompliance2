from django.urls import include, path
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url


routers=DefaultRouter()
routers.register(r'login',views.loginViewset)
routers.register(r'cal',views.calculationViewset)
routers.register(r'getdetails',views.FileView,basename='getdetails')
routers.register(r'getcompiled',views.FileView2,basename='getcompiled')
routers.register(r'notify',views.getNotify)

urlpatterns=[
    path('',views.mainfunc),
    path('post_details/',views.post),
    path('post_template/',views.post_template),
    # path('file/',views.file_upload),
    # url(r'^upload/$', FileView.as_view(), name='file-upload'),
    path('filter/<int:id>/',views.filter_table),
    path('update/',views.updatedesc.as_view()),


]

urlpatterns+=routers.urls