from django.shortcuts import render
from second.models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    context = {
        'items' : Post.objects.all()
    }
    return render(request, 'second/list.html' , context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/second/list/')
    form = PostForm()
    return render(request, 'second/create.html', {'form' : form})

def confirm(request):
    form = PostForm(request.POST) #클래스 인스턴스 생성
    if form.is_valid(): #Exception이 있는지 검사
        return render(request, 'second/confirm.html', {'form' : form})
    return HttpResponseRedirect('/create/')