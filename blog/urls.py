"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import static

from blog.settings import PAGE_SIZE, DISPLAY
from help_tools.Helper import iPagination
from user.models import Category, ArticleInfo, TagInfo


def index(request):
    print(111111)
    cate_name = Category.objects.all().order_by('id')
    return render(request, 'index.html', {
        # 'all_category': all_category,
        # 'new_articles': new_articles,
        # 'recommend_article': recommend_article,
        # 'all_articles': all_articles,
        # 'all_tags': all_tags,
        # 'new_category': new_category,
        # 'pages': pages,
        # 'all_day': all_day,
        # 'article_total': article_total,
        'cate_name': cate_name
    })


def search(request):
    print(111111)
    all_category = Category.objects.filter(is_tab=True).order_by('id')
    cont = request.GET.get('keyword', '')
    if not cont:
        return render(request, 'none.html', {
            'all_category': all_category
        })
    page = int((request.GET.get('p', 1)))
    offset = (page - 1) * PAGE_SIZE
    all_articles = ArticleInfo.objects.filter(title__icontains=cont).order_by('-id')[offset:offset + PAGE_SIZE:]
    all_tags = TagInfo.objects.all().order_by('-id')
    if not all_articles:
        return render(request, 'none.html', {
            'all_category': all_category
        })

    page_params = {
        'total': ArticleInfo.objects.filter(title__icontains=cont).order_by('-id').count(),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': DISPLAY,
        'url': request.path.replace('&p={}'.format(page), '?')
    }
    pages = iPagination(page_params)

    # all_articles = all_articles[offset:offset + PAGE_SIZE:]

    return render(request, 'search_list.html', {
        'all_category': all_category,
        'all_articles': all_articles,
        'cont': cont,
        # 'new_articles': new_articles,
        'all_tags': all_tags,
        'pages': pages,
    })

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('apps.user.urls')),
    url(r'^$', index, name='index'),
    url(r'^search/$',search,name='search'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')
]
# urlpatterns += staticfiles_urlpatterns()