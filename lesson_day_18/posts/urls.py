from django.urls import path 
from .views import HomePageView
from .views import ActorPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("/actor/", ActorPageView.as_view(), name="actor" )
]
