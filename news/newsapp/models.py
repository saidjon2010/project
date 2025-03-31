from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
#  Create your models here.




class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail_url',kwargs={'slug':self.slug})



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()  
    date = models.DateTimeField(default=timezone.now,null=True) 
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True)
    popular = models.IntegerField(default=1 ,null=True)
   

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})



class Comment(models.Model):
    postss = models.ForeignKey(Post, on_delete = models.CASCADE , null = True , related_name = 'comments')
    author_name = models.CharField('author_name' , max_length = 50)
    comment_text = models.TextField('comment' , max_length = 1000)

    def __str__(self):
        return 'USER:' + self.author_name + '-- ' + self.comment_text

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'