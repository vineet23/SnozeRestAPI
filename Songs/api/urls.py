from django.conf.urls import url

from .views import Song_API_View

urlpatterns = [
    #T0 get API view of Songs
    url(r'^songs/$', Song_API_View.as_view(), name='songs'),
]