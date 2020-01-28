from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name="posts_list"),
    path('post/<int:id>/', views.PostDetailView.as_view(), name="post_detail"),
]