from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
