# from django import forms
# from django.utils.html import format_html
# from django.contrib import admin
# from .models import FeedbackModel, HistoryEntry, ValidatedImage

# # Modifier le titre de la page d'administration
# admin.site.site_header = "Administration du Projet"
# admin.site.site_title = "Interface Admin"
# admin.site.index_title = "Bienvenue sur le panneau d'administration"



# # FeedbackModel Admin Configuration
# @admin.register(FeedbackModel)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('predicted_class', 'suggested_class', 'date', 'latitude', 'longitude', 'validated', 'image_preview')
#     list_filter = ('validated', 'date')
#     search_fields = ('predicted_class', 'suggested_class')
#     readonly_fields = ('image_display',)

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" />', obj.image.url)
#         return "No Image"
#     image_preview.short_description = 'Aperçu de l\'image'

#     def image_display(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" />', obj.image.url)
#         return "No Image"
#     image_display.short_description = 'Affichage de l\'image'

# # HistoryEntry Admin Configuration
# @admin.register(HistoryEntry)
# class HistoryEntryAdmin(admin.ModelAdmin):
#     list_display = ('prediction', 'confidence', 'date', 'latitude', 'longitude', 'image_preview')
#     list_filter = ('date',)
#     search_fields = ('prediction', 'image_path')
#     readonly_fields = ('image_display',)

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" />', obj.image.url)
#         return "No Image"
#     image_preview.short_description = 'Aperçu de l\'image'

#     def image_display(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" />', obj.image.url)
#         return "No Image"
#     image_display.short_description = 'Affichage de l\'image'

# # ValidatedImage Admin Configuration
# @admin.register(ValidatedImage)
# class ValidatedImageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'predicted_class', 'created_at')
#     list_display_links = ('name',)
#     list_filter = ('predicted_class', 'created_at')
#     search_fields = ('name', 'predicted_class')
#     fields = ('name', 'image', 'predicted_class', 'created_at')
#     readonly_fields = ('created_at',)

#     form = forms.modelform_factory(
#         ValidatedImage,
#         fields="__all__",
#         widgets={
#             'predicted_class': forms.TextInput(attrs={'placeholder': 'Classe prédite'}),
#         }
#     )
from django import forms
from django.utils.html import format_html
from django.contrib import admin
from .models import FeedbackModel, HistoryEntry, ValidatedImage


# Customize the admin panel
admin.site.site_header = "Project Administration"
admin.site.site_title = "Admin Interface"
admin.site.index_title = "Welcome to the Admin Panel"


# Reusable Mixin for Image Previews
class ImagePreviewMixin:
    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return format_html('<span style="color: red;">No Image</span>')
    image_preview.short_description = 'Image Preview'

    def image_display(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="max-height: 300px; max-width: 300px;" />', obj.image.url)
        return format_html('<span style="color: red;">No Image</span>')
    image_display.short_description = 'Image Display'


# FeedbackModel Admin Configuration
@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ('predicted_class', 'suggested_class', 'date', 'latitude', 'longitude', 'validated', 'image_preview')
    list_filter = ('validated', 'date', 'latitude', 'longitude')
    search_fields = ('predicted_class', 'suggested_class')
    readonly_fields = ('image_display',)


# HistoryEntry Admin Configuration
@admin.register(HistoryEntry)
class HistoryEntryAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ('prediction', 'confidence', 'date', 'latitude', 'longitude', 'image_preview')
    list_filter = ('date', 'latitude', 'longitude')
    search_fields = ('prediction',)
    readonly_fields = ('image_display',)



# # ValidatedImage Admin Configuration
# @admin.register(ValidatedImage)
# class ValidatedImageAdmin(admin.ModelAdmin, ImagePreviewMixin):
#     list_display = ('id', 'name', 'predicted_class', 'image_preview', 'latitude', 'longitude', 'validated_at')
#     list_filter = ('validated_at', 'predicted_class', 'latitude', 'longitude')  
#     search_fields = ('name', 'predicted_class')
#     eadonly_fields = ('image_display',)


@admin.register(ValidatedImage)
class ValidatedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'predicted_class', 'image_preview', 'latitude', 'longitude', 'validated_at')
    list_filter = ('validated_at', 'predicted_class', 'latitude', 'longitude')
    search_fields = ('name', 'predicted_class')
    readonly_fields = ('validated_at',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return format_html('<span style="color: red;">No Image</span>')
    image_preview.short_description = 'Image Preview'