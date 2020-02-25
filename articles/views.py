from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def articleList(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/articleList.html', {'articles': articles})


def articleDetail(request, slug):
    return HttpResponse(slug)
# Create your views here.
