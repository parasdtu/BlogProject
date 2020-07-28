from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# ,default='blog_pics/django-logo-negative.png'
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    blogger_name=models.CharField(max_length=256,default="BloggerName")
    blog_pic_1=models.ImageField(upload_to='blog_pics/',blank=True,default='blog_pics/django-logo-negative.png')
    text_1=models.TextField(blank=True,null=True)
    blog_pic_2=models.ImageField(upload_to='blog_pics/',blank=True)
    text_2=models.TextField(blank=True,null=True)
    blog_pic_3=models.ImageField(upload_to='blog_pics/',blank=True)
    text_3=models.TextField(blank=True,null=True)
    tag_1=models.CharField(max_length=256,blank=True)
    tag_2=models.CharField(max_length=256,blank=True)
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)
    # blog_pic=models.ImageField(upload_to='blog_pics/',blank=True,default='blog_pics/django-logo-negative.png')

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text_1[:80]

class Comment(models.Model):
    post=models.ForeignKey('basic_app.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=256)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comments=models.BooleanField(default=False)

    def approve(self):
        self.approved_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
# class Subscription(models.Model):
#     mail_id=models.EmailField(max_length=254)
