from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context