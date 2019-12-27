from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns=[
    url(r'^register/',views.user_registration,name='register'),
    url(r'^login/',views.user_login,name='user_login'),
    url(r'^postview',views.PostListView.as_view(),name='post_view'),
    url(r'^profilepage/',views.profile_page_reverse,name='profile_page'),
    ]
