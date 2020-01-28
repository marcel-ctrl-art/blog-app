from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post


class PostListView(View):
    def get(self, request):
        template_name = "posts_list.html"
        posts = Post.objects.all().order_by("created_at")
        paginator = Paginator(posts, 3)
        page = request.GET.get("page")
        posts = paginator.get_page(page)
        ctx = {
            "posts": posts
        }
        return render(request, template_name, ctx)


class PostDetailView(View):
    def get(self, request, id):
        template_name = "post_detail.html"
        post = get_object_or_404(Post, pk=id)
        ctx = {"post": post}
        return render(request, template_name, ctx)