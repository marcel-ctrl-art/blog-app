from django.contrib import messages
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
        paginator = Paginator(posts, 5)
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
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            author = form.cleaned_data["author"]

            new_post = Post.objects.create(title=title, text=text, author=author)
            new_post.save()

            return redirect(f"/post/{new_post.pk}")


class EditPostView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        template_name = "edit_post.html"
        msg = "Edit your post"
        form = NewPostForm(instance=post)
        ctx = {
            "msg": msg,
            "form": form,
            }
        return render(request, template_name, ctx)

    def post(self, request, id):
        post = get_object_or_404(Post, pk=id)
        template_name = "edit_post.html"
        form = NewPostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "You successfully updated the post")
            ctx = {"form": form}
            return redirect(f"/post/{post.pk}")

        else:
            ctx = {
                "form": form,
                "error": "The form was not updated successfully. Please enter in a title and content",
            }
            return render(request, template_name, ctx)


class DeletePostView(View):
    def get(self, request, id):
        post_to_del = get_object_or_404(Post, pk=id)
        template_name = "post_delete.html"
        ctx = {"post_to_del": post_to_del}
        return render(request, template_name, ctx)

    def post(self, request, id):
        template_name = "post_delete.html"
        post_to_del = get_object_or_404(Post, pk=id)

        if request.POST.get("delete"):
            post_to_del.delete()
            msg = "Yor post has been deleted."

        ctx = {
            "post_to_del": post_to_del,
            "msg": msg,
        }

        return render(request, template_name, ctx)
