from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'Posts/posts_page.html', context=context)


@login_required
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
        'date_post': post.date_posted,
    }
    return render(request, 'Posts/post.html', context=context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post', post_id=post.id)
        else:
            if not form.cleaned_data.get('image_post'):
                form.add_error('image_post', 'This field is required.')
    else:
        form = PostForm()
    context = {
        'form': form,
        'title': "Create Post"
    }
    return render(request, 'Posts/form_post.html', context=context)


@login_required()
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'title': "Update Post",
        'update': 1,
        'post': post
    }
    return render(request, 'Posts/form_post.html', context=context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff or u)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_superuser:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    elif request.user.is_staff and not post.user.is_superuser:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    elif request.user == post.user:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this post.')
    return redirect('home')
