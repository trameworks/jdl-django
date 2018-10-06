from django.conf.urls import url, include
from jardins.core.views import HomeView as home, register_workshop


urlpatterns = [
    url(r'^$', home.as_view(), name='home_page'),
    url(r'^ajax/register_workshop$', register_workshop, name='register_workshop'),
]
