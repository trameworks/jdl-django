"""jardins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.static import serve
from django.views import defaults as default_views
from jardins.core import urls as core_urls
from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    url(r'', include((core_urls, 'core'), namespace='core')),
    url('^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls for testing purposes
if settings.DEBUG:
    # STATIC URL
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve ,{'document_root': settings.STATIC_ROOT}))
    # add django admin on debug mode to register some data
    # from django.contrib import admin
    # urlpatterns.append(url('^admin/', admin.site.urls))

    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),

        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),

        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),

        url(r'^500/$', default_views.server_error),
    ]
