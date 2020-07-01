from django.shortcuts import render, reverse, HttpResponseRedirect
from g_post.models import Post
from g_post.forms import AddPostForm
import subprocess

# Create your views here.
def index(request):
    data = Post.objects.order_by('-date')
    return render(request, 'index.html', {'data': data})

def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                post_type = data['post_type'],
                post = data['post'],
                upVote=0,
                downVote=0
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, 'AddPostForm.html', {'form': form})

def upVote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upVote += 1
    post.totalVote +=1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def downVote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downVote += 1
    post.totalVote -=1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def high_to_low(request):
    data = Post.objects.order_by('-upVote')
    return render(request, 'filters.html', {'data': data})


def low_to_high(request):
    data = Post.objects.order_by('upVote')
    return render(request, 'filters.html', {'data': data})

def roast(request):
    data= Post.objects.filter(post_type=False).order_by('-date')
    return render(request, 'filters.html', {'data':data})

def boast(request):
    data = Post.objects.filter(post_type=True).order_by('-date')
    return render(request, 'filters.html', {'data':data})







