from django.contrib import admin
from .models import Blog, Category, Main
from django.utils.html import format_html


# Register your models here.

# admin.site.register(Blog)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    ordering = ['name']


@admin.register(Main)
class AdminMain(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'status']
    search_fields = ['title', 'status']
    actions = ['update_status_active', 'update_status_deactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}

    def show_image(self, object):
        return format_html('<img src="{}" width="40px">', format(object.image.url))

    show_image.short_description = 'image'

    def update_status_active(self, request, queryset):
        queryset.update(status=True)

    update_status_active.short_description = 'Active'

    def update_status_deactive(self, request, queryset):
        queryset.update(status=False)

    update_status_deactive.short_description = 'Deactive'


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'status']
    search_fields = ['title', 'status']
    actions = ['update_status_active', 'update_status_deactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'

    def show_image(self, object):
        return format_html('<img src="{}" width="40px">', format(object.image.url))

    show_image.short_description = 'image'

    def update_status_active(self, request, queryset):
        queryset.update(status=True)

    update_status_active.short_description = 'Active'

    def update_status_deactive(self, request, queryset):
        queryset.update(status=False)

    update_status_deactive.short_description = 'Deactive'
