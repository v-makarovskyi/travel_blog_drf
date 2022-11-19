from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models 

admin.site.register(models.Category, MPTTModelAdmin)

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'owner', 'post']

    

