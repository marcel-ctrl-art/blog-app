from django.core.paginator import Paginator
from django.shortcuts import render
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