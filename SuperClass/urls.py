from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SuperClass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #default to index
    #url(r'^courses/', include('courses.urls')),
    url(r'^index/$', 'courses.views.index', name='index'),
    url(r'^new/$', 'courses.views.new', name='new'),
    url(r'^code/$', 'courses.views.code'),
    url(r'^article/$', 'courses.views.articles'),
    url(r'^article/new/$', 'courses.views.newArticle'),
    #/1 => show
    url(r'^article/(?P<article_id>\w+)/$', 'courses.views.article'),
    
)
