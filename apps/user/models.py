import random
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models, connection


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='用户昵称', null=True, blank=True)
    image = models.ImageField(upload_to='user/%y/%m/%d', verbose_name='头像', max_length=200, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_start = models.BooleanField(default=False, verbose_name='是否激活')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class PersonManager(models.Manager):

    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""SELECT DISTINCT first_name FROM people_person WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objects = PersonManager()


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    click_num = models.IntegerField(default=0)
    person = models.ForeignKey(Person, related_name='blog_person', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客模块'
        verbose_name_plural = verbose_name
        db_table = 'bloginfo'


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_tab = models.BooleanField(default=True, verbose_name='是否导航')
    title = models.CharField(max_length=50, verbose_name='类别标题', null=True, blank=True)
    path_name = models.CharField(max_length=15, verbose_name='路径别名', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别表'
        verbose_name_plural = verbose_name


class TagInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    category = models.ForeignKey(Category, verbose_name='所属类别', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class ArticleInfo(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.TextField(max_length=80, verbose_name='简介')
    content = models.TextField(verbose_name='文章内容')
    # content = UEditorField(verbose_name='文章内容', width=1200, height=400, toolbars='full', imagePath='ueditor/image/'+m_y+'/'+m_m+'/',
    #             filePath='ueditor/files/'+m_y+'/'+m_m+'/', upload_settings={'imageMaxSizing': 1024000}, default='')
    click_num = models.IntegerField(default=0, verbose_name='浏览数')
    cont_num = models.IntegerField(default=0, verbose_name='评论数')
    love_num = models.IntegerField(default=0, verbose_name='点赞数')
    image = models.ImageField(upload_to='article/%y/%m/%d', verbose_name='封面', max_length=200,
                              default='article/default' + str(random.choice('12345')) + '.jpg', null=True, blank=True)
    author = models.ForeignKey(UserProfile, verbose_name='文章作者')
    category = models.ForeignKey(Category, verbose_name='所属类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
    is_recommend = models.BooleanField(default=False, verbose_name='首页推荐')
    taginfo = models.ForeignKey(TagInfo, verbose_name='所属标签', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

# Person.objects.first_names('Lennon')
