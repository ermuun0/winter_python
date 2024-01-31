from django.views.generic import ListView
from .models import Post
from .models import Actor
# Create your views here.
class HomePageView(ListView):
     model = Post
     template_name = "home.html"
class ActorPageView(ListView):
    model = Actor
    template_name = "actor.html"