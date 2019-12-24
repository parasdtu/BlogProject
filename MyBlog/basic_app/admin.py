from django.contrib import admin
from basic_app.models import UserProfileInfo,CommentModel,NewPostModel
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(NewPostModel)
admin.site.register(CommentModel)
