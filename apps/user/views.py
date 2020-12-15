from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from apps.user.models import Blog
from django.db import connection


def index(request):
    # print(1,connection.queries)
    # blog_obj = Blog.objects.create(title="python异常", content="讲解python异常处理")
    all_queryset = Blog.objects.all()
    # print(2,connection.queries)
    print(all_queryset)
    cursor = connection.cursor()
    cursor.execute("""select * from bloginfo where id=%s""", [1])
    # cursor.execute("""select * from bloginfo""")
    row = cursor.fetchall()
    print('row', row)
    # print('blog_obj',blog_obj)

    return HttpResponse('我是user主页！')