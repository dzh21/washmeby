from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from leaflet.forms.widgets import LeafletWidget
from .models import CarWash


class WashesIndex(TemplateView):
    model = CarWash
    template_name = "carwash/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(WashesIndex, self).get_context_data(**kwargs)
        context['carwashes'] = CarWash.objects.all()
        return context


class OwnersWashesListView(LoginRequiredMixin, TemplateView):
    login_url = '/userauth/login/'
    redirect_field_name = 'next'

    model = CarWash
    template_name = "carwash/carwashes.html"

    def get_context_data(self, **kwargs):
        context = super(OwnersWashesListView, self).get_context_data(**kwargs)
        context['carwashes'] = CarWash.objects.filter(fk_owner=self.request.user.id)
        return context


class OwnersWashesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/userauth/login/'
    redirect_field_name = 'next'

    model = CarWash

 
class OwnersWashesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/userauth/login/'
    redirect_field_name = 'next'

    model = CarWash
    success_url = '/carwashes/'
    fields = ['address', 'geom']
    

class OwnersWashesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/userauth/login/'
    redirect_field_name = 'next'

    model = CarWash
    success_url = '/carwashes/'
    fields = ['address', 'geom']

    def form_valid(self, form):
        carwash = form.save(commit=False)
        carwash.fk_owner = self.request.user
        return super(OwnersWashesCreateView, self).form_valid(form)
        
