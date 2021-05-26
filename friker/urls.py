from django.conf.urls import url
from django.contrib import admin
from photos import views as photo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', photo_views.home)
]
