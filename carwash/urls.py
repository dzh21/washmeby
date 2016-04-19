from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CarWashList.as_view()),
]
