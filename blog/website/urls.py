from django.urls import path, include
from .views import hello_blog, save_form
from .views import post_detail

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save_form/', save_form, name='save_form'),
]
