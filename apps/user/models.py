from django.db import models, connection


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    click_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客模块'
        verbose_name_plural = verbose_name
        db_table = 'bloginfo'




class PersonManager(models.Manager):

    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""SELECT DISTINCT first_name FROM people_person WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objects = PersonManager()

# Person.objects.first_names('Lennon')