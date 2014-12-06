from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from django.core.urlresolvers import reverse
from agency import views
from agency.views import  EstateDetailView, PageDetailView


urlpatterns = [
    # Examples:
    # url(r'^$', 'estate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search),
    url(r'^(?P<slug>[\w\-]+)/$', PageDetailView.as_view()),
    
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<slug>[\w\-]+)/$', EstateDetailView.as_view()),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^tinymce/', include('tinymce.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
