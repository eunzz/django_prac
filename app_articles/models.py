from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200, verbose_name="제목")
  content = models.TextField(verbose_name="내용")
  img = models.ImageField(blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
        return self.title

  tag_set = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
