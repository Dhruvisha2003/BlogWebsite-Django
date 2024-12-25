from django.shortcuts import *
from .models import slide, blog, Myprofile, category, cmt

# Create your views here.


def index(request):

    data = slide.objects.all()
    blogs = blog.objects.all().order_by("-date")
    latest = blogs[:5]
    data1 = Myprofile.objects.all()
    cat = category.objects.all()
    return render(
        request,
        "index.html",
        {"data": data, "blogs": blogs, "data1": data1, "cat": cat, "latest": latest},
    )


def about(request):
    cat = category.objects.all()
    blogs = blog.objects.all().order_by("-date")
    pic1 = blogs[:3]
    return render(request, "About-me.html", {"cat": cat, "pic1": pic1})


def contact(request):
    data1 = Myprofile.objects.all()

    return render(request, "Contact.html", {"data1": data1})


def Me(request):
    data1 = Myprofile.objects.all()
    return render(request, "Profile.html", {"data1": data1})


def post(request, id):
    try:
        post_id = blog.objects.get(id=id)
        print(post_id)
        # blog_id = post_id
        # print(blog_id.id)
    except blog.DoesNotExist:
        return HttpResponse("Blog post not found", status=404)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("msg")
        sub = request.POST.get("sub")

        saved = cmt(name=name, email=email, msg=msg, sub=sub, blog_id=post_id.id)
        saved.save()
        # return redirect("post_data", id=post_id.id)
    comments = cmt.objects.filter(blog_id=post_id.id).distinct()
    return render(
        request,
        "Single-post.html",
        {
            "image": post_id.image,
            "category": post_id.category,
            "date": post_id.date,
            "title": post_id.title,
            "desc": post_id.desc,
            "comments": comments,
        },
    )
