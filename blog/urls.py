from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('post/<int:id>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),
]