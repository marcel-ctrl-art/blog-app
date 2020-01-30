from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import CreateView

from .forms import NewPostForm
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


class CreatePostView(View):
    def get(self, request):
        template_name = "add_new_post_form.html"
        form = NewPostForm()
        return render(request, template_name, {"form": form})

    def post(self, request):
        form = NewPostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']

            new_post = Post.objects.create(title=title, text=text, author=author)
            new_post.save()

            return redirect(f"/post/{new_post.pk}")

