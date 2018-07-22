from django.shortcuts import render
from .models import Article


# Create your views here.
def detail_article(request,pk):
  article = Article.objects.get(pk=pk)
  ctx = {
    'article': article
  }
  return render(request, 'app_articles/detail.html', ctx)


def list_article(request):
  article = Article.objects.all()
  ctx ={
    'article' : article
  }
  return render(request,'app_articles/list.html', ctx)