from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUptadeView, ArticleDeleteView
urlpatterns = [
    path("", ArticleListView.as_view(), name="arcticle_list"),
    path("<int:pk>/edit/", ArticleUptadeView.as_view(), name = "article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name = "article_delete"),
    path("<int:pk/", ArticleDetailView.as_view(), name="article_detail")
]
