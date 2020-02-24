from django.shortcuts import render
from .models import Article

def articleList(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/articleList.html', {'articles': articles})
# Create your views here.
