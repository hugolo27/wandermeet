from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from wandermeet.fake import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexPage.as_view(), name='wandermeet'),
    url(r'^chat', ChatPage.as_view(), name='wandermeet'),
    url(r'^login/', LoginPage.as_view(), name='wandermeet'),
    url(r'^profile/', ProfilePage.as_view(), name='wandermeet'),
    url(r'^map/', MapPage.as_view(), name='wandermeet'),
]

urlpatterns += staticfiles_urlpatterns()
