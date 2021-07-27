from django.conf.urls import url
from rango import views

app_name = 'rango'
urlpatterns = [
url('', views.index, name='index'),
]