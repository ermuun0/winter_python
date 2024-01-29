from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class ActorListPageView(TemplateView):
    template_name = "actor_list.html"
    
class InfoPageView(TemplateView):
    template_name = "info.html"
