from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.first_name

class NewPostModel(models.Model):
    author=models.ForeignKey(UserProfileInfo,related_name='posts',on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    text=models.CharField(max_length=2048)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    title=models.ForeignKey(NewPostModel,related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=256)
    text=models.CharField(max_length=2048)

    def __str__(self):
        return self.author
