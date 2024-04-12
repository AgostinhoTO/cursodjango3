from django.contrib import admin
from website.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'sub_title', 'full_name', 'categories', 'deleted'
    ]
    search_fields  = ['title', 'sub_title']

    # ESTA FUNCAO JA EXISTE, VAMOS SOBRESCREVER
    def get_queryset(self, request):
        return Post.objects.filter(deleted=True)


# Register your models here.
admin.site.register(Post, PostAdmin)
