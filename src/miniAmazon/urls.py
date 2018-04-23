"""amazonSim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#static_cdn static

from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url
from django.contrib import admin

from goods.views import GoodListView, good_list_view, GoodDetailView, good_detail_view

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', home_page),
    url(r'^about/$', about_page),
    url(r'^contact/$', contact_page),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^goods/$', GoodListView.as_view()),
    url(r'^goods-fbv/$',good_list_view),
    url(r'^goods/(?P<pk>\d+)/$', GoodDetailView.as_view()),
    url(r'^goods-fbv/(?P<pk>\d+)/$',good_detail_view),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)