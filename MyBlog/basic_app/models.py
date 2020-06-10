from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)
    blog_pic=models.ImageField(upload_to='blog_pics/',blank=True,default='blog_pics/django-logo-negative.png')

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
        return self.text[:50]

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
