from django.contrib import admin
from .models import slide,blog,Myprofile,category,comment

# Register your models here.

admin.site.register(slide)
admin.site.register(blog)
admin.site.register(Myprofile)
admin.site.register(category)
admin.site.register(comment)
