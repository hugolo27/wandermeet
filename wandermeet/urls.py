from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from wandermeet.fake import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^/*', HomePage.as_view(), name='becor'),
]

urlpatterns += staticfiles_urlpatterns()
