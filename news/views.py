from django.shortcuts import render
from .models import News


def base(request):
    news = News.objects.all()
    return render(request,'news/base.html',
            {'news': news},
            )


def kontakt(request):
    return render(request, 'news/kontakt.html', {})