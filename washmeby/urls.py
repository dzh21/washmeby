
from django.conf.urls import url, include
from django.contrib import admin
from .views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="home"),
    url(r'^carwashes/', include('carwash.urls')),
    url(r'^userauth/', include('userauth.urls')),
]
