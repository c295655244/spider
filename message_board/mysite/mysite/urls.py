 #coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.messageboard.models import *
from django.views.generic.list import  ListView
from mysite.messageboard  import models
from messageboard.views import mains,register_page
from django.views.generic import TemplateView
from django.contrib.auth.views import login,logout
from django.contrib.auth.views import *
from messageboard.views import msg_post_page




admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^mains/$', ListView.as_view(
    #	model=models.MsgPost,
    #	paginate_by=10,#留言对象列表的分页处理。
    #	template_name= 'main.html',# 模板文件名称。
    #	context_object_name= 'main.html'# 对象列表的模板变量名称
    #	)),#实现分页显示所有用户发 表 留 言 的 列 表 
    url(r'^$', mains),   
    url(r'^mains/$',mains),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mains/register/$', register_page),
    url(r'^main/register/success/$', TemplateView.as_view(
    	template_name= 'register_success.html')),
    url(r'^accounts/login/$', login),
    url(r'^mains/logout/$',logout,{'next_page':'/mains/'}), #退出后跳转到主页
    url(r'^mains/password/change/$', password_change,{'template_name':'registration/password_change.html','post_change_redirect': 'mains/password/change/done/'}),
    url(r'mains/password/change/done/$', password_change_done,{'template_name':'registration/password_change_success.html'}),
    url(r'^mains/post/$', msg_post_page),
)
