from django.shortcuts import render
from django.views.generic import ListView
from .models import PlansMonth, PlansDay
from .logic import day
# Create your views here.

class Plans(ListView):
    template_name = 'main/index.html'
    model = PlansMonth
    context_object_name = 'planemonth'

    def get_queryset(self):
        return PlansMonth.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context