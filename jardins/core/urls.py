from django.conf.urls import url, include
from jardins.core.views import HomeView as home


urlpatterns = [
    url(r'^$', home.as_view(), name='home_page'),
]
