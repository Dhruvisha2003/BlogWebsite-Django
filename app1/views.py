from django.shortcuts import *
from .models import slide,blog,Myprofile,category

# Create your views here.

def index(request):
     
    data = slide.objects.all()
    blogs = blog.objects.all().order_by('-date')
    latest = blogs[:5]
    data1 = Myprofile.objects.all()
    cat = category.objects.all()
    return render(request,'index.html',{'data':data,'blogs':blogs,'data1':data1,'cat':cat,'latest':latest})

def about(request):
    return render(request,'About-me.html')

def contact(request):
    return render(request,'Contact.html')

def Me(request):
    data1 = Myprofile.objects.all()
    return render(request,'Profile.html',{'data1':data1})

def post(request,id):
    post_id = blog.objects.get(id=id)
    print(post_id.date)
    return render(request,'Single-post.html',{'image' : post_id.image,'category' : post_id.category,'date' : post_id.date, 'title' : post_id.title,'desc' : post_id.desc})