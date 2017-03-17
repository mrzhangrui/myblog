"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$',blog_views.home),
	url(r'^signin/$',blog_views.signin),
	url(r'^register/$',blog_views.register),
	url(r'^signout/$',blog_views.signout),
    url(r'^blogs/$',blog_views.blogs),
    url(r'^blog/(?P<name>\w+)/$',blog_views.blog),
    url(r'^blogs/delete/(?P<name>\w+)/$',blog_views.delete),
    url(r'^blogs/change/(?P<name>\w+)/$',blog_views.change),
    url(r'^blogs/create/$',blog_views.create_blog),
    url(r'^comments/$',blog_views.comments),
    url(r'^yonghu/$',blog_views.yonghu_list),
    url(r'^comment/delete/?P<name>\w+$',blog_views.comment_delete),
    url(r'^yonghu/delete/?P<username>\w+$',blog_views.yonghu_delete),
]
