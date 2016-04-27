from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.WashesIndex.as_view(), name='home'),
    url(r'^$', views.OwnersWashesListView.as_view(), name='carwashes_list'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.OwnersWashesDeleteView.as_view(), name='carwashes_del'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.OwnersWashesUpdateView.as_view(), name='carwashes_edit'),
    url(r'^create/$', views.OwnersWashesUpdateView.as_view(), name='carwashes_new'),
]
