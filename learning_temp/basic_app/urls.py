from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    url(r'^url_temp/$',views.url_temp,name='url_temp'),
    url(r'^other/$',views.other,name='other'),
]
