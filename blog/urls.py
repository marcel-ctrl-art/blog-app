from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('post/<int:id>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.CreatePostView.as_view(), name="post_new"),
    path('post/edit/<int:id>/', views.EditPostView.as_view(), name="post_edit"),
    path('post/delete/<int:id>/', views.DeletePostView.as_view(), name="post_delete"),
    path('post/delete_completed/', views.DeletedPostView.as_view(), name="post_deleted"),
]