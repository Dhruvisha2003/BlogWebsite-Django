from django.contrib import admin
from .models import slide,blog,Myprofile,category,cmt

# Register your models here.

admin.site.register(slide)
admin.site.register(blog)
admin.site.register(Myprofile)
admin.site.register(category)
admin.site.register(cmt)
