from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Imageclass


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]

    class Meta:
        model = Imageclass


admin.site.register(Imageclass, ImageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'image',
    ]
    list_display = (
        'id',
        'name',
        'admin'
    )


    def save_form(self, request, form, change):
        category = form.save(commit=False)
        category.admin = request.user
        category.save()

        return super().save_form(request, form, change)

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)