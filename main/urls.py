from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.post_detail, name='post-detail'),
]
