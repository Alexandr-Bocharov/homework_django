from django.contrib import admin


from blogs.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'views_count')
    list_filter = ('public_sign',)
    search_fields = ('title', 'body')





