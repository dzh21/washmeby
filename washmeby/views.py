from django.views.generic import TemplateView
from carwash.models import CarWash


class Index(TemplateView):
    model = CarWash
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['carwashes'] = CarWash.objects.all()
        return context
