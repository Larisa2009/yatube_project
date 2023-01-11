from django.contrib import admin

from .models import Post, Group

list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
list_editable = ('group',)
search_fields = ('text',)
list_filter = ('pub_date',)
empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk'
        'title',
        'slug',
        'description'
    )
    list_editable = ('title',)
    search_fields = ('description',)
    empty_value_display = '-пусто-'     


admin.site.register(Post, PostAdmin) 
admin.site.register(Group, GroupAdmin)