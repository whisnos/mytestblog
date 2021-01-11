import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden
# Create your views here.
from user.models import Blog, Category
from django.db import connection


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
    # print(1,connection.queries)
    # blog_obj = Blog.objects.create(title="python异常", content="讲解python异常处理")
    all_queryset = Blog.objects.all().values('title')
    json.dumps(all_queryset)
    # print(2,connection.queries)
    print(all_queryset)
    cursor = connection.cursor()
    cursor.execute("""select * from bloginfo where id=%s""", [1])
    # cursor.execute("""select * from bloginfo""")
    row = cursor.fetchall()
    print('row', row)
    # print('blog_obj',blog_obj)

    # return JsonResponse('我是user主页！')
    qs = json.dumps(list(all_queryset),ensure_ascii=True,indent=4,separators=(',',':'))
    # return JsonResponse(list(all_queryset),safe=False,json_dumps_params={'ensure_ascii':False})
    return HttpResponse(qs, content_type='application/json')
    return HttpResponseForbidden('Hi Debug5.com', content_type='application/json; charset=UTF-8')
    return HttpResponseBadRequest('错误请求')
    return HttpResponseForbidden('/')


def test_json(request):
    data = {
        'name': 'debug5',
        'age': 3,
    }
    listdata = [1, 2, 3, 4, 5]
    return JsonResponse(listdata) # , safe=False
    return HttpResponse(json.dumps(data), content_type="application/json")


def user_register(request):
    return HttpResponse('user_register')


def user_login(request):
    return HttpResponse('user_login')

def user_logout(request):
    return HttpResponse('user_logout')

def user_center(request):
    return HttpResponse('user_center')