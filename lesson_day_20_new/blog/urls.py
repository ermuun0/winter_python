from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUptadeView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name ='home'),
    path("post/new/", BlogCreateView.as_view(), name='post_new'),
    path("post/<int:pk>/edit/", BlogUptadeView.as_view(), name="post_edit")
]