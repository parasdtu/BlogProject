from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns=[
    url(r'^register/',views.user_registration,name='register'),
    url(r'^login/',views.user_login,name='user_login'),
]
