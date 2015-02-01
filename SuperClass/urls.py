from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SuperClass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #default to index
    #url(r'^courses/', include('courses.urls')),
    #url(r'^index/$', 'courses.views.index', name='index'),
    #url(r'^new/$', 'courses.views.new', name='new'),
    #url(r'^code/$', 'courses.views.code'),
    url(r'^accept/$', 'courses.views.accept'),

    #for normal users
    url(r'^article/index/$', 'courses.views.articles'),
    url(r'^article/(?P<article_id>\w+)/$', 'courses.views.article'),

    #for admin
    url(r'^admin/article/index/$', 'courses.views.index'),
    url(r'^admin/article/new/$', 'courses.views.new'),
    url(r'^admin/article/(?P<article_id>\w+)/$', 'courses.views.review'),
    url(r'^admin/article/(?P<article_id>\w+)/publish/$', 'courses.views.publish'),
    url(r'^admin/article/(?P<article_id>\w+)/delete/$', 'courses.views.delete'),
    
)
