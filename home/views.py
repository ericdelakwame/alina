from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.urls import reverse_lazy
from django.views.generic.edit import (
   UpdateView, FormView, DeleteView, FormMixin
)




class IndexView(TemplateView):
    template_name = 'home/index.html'
    
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        return context

    
class PrivacyPolicy(TemplateView):
    template_name = 'home/privacy_policy.html'
    
class TermsAndConditions(TemplateView):
    template_name = 'home/terms_conditions.html'
    
class CancellationPolicy(TemplateView):
    template_name = 'home/cancellation_policy.html'


class ManifestoView(TemplateView):
    template_name = 'home/manifesto.html'
    


class PressView(TemplateView):
    template_name = 'home/press.html'
