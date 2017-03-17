from django.contrib import admin

# Register your models here.
from blog.models import Blog,Comment

class BlogAdmin(admin.ModelAdmin):
	list_display=('name','summary')
	search_fields=('name','summary')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)