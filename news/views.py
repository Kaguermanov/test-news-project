from django.shortcuts import render, get_object_or_404
from .models import Article

def news_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Сортировка по убыванию даты
    return render(request, 'news_list.html', {'articles': articles})

def news_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'news_detail.html', {'article': article})
from django.shortcuts import render

# Create your views here.
