from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    
class ArticleDetailView(DetailView):
    model= Article
    template_name = "article_detail.html"
    
class ArticleUptadeView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ("title", "body")

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_listß")
    
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author"
    )