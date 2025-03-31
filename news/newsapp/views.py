from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Post,Category
from .forms import RegistrationForm
from django.db.models import Q
# Create your views here.


def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    popular = Post.objects.filter(popular__gte=10)
    return render(request,'index.html',{'posts':posts,'category':category,'popular':popular})


def post_detail(request,slug):
    postss = Post.objects.get(slug__iexact=slug)
    postss.popular+=1
    postss.save()
    return render(request,'post_detail.html',{'postss':postss})


def category_detail(request,slug):
    categories = Category.objects.get(slug__iexact=slug)
    return render(request,'category_detail.html',{'categories':categories})


def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains = query) | Q(description__icontains = query)
    )
    return render(request,'search.html',{'query':query,'search_obj':search_obj})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})



def leave_comment(request, slug):
    try:
        postss = Post.objects.get(slug__iexact = slug)
    except:
        raise Http404("Article not found")
    if request.user.is_authenticated:
        user = request.user.username
        postss.comments.create(author_name = user , comment_text = request.POST.get('comment_text'))
    else:
        postss.comments.create(author_name = request.POST.get('name'), comment_text = request.POST.get('comment_text'))
        
    return HttpResponseRedirect(reverse('post_detail_url' , args = (postss.slug,)))