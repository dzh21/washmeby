from django.conf.urls import url, include
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='login'
    ), name='register'),
]
