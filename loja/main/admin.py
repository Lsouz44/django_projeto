from django.contrib import admin

from.models import Banner,Category, Marca, Color, Size, Product, ProductAttribute

admin.site.register(Marca)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag_path')
admin.site.register(Banner, BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag_path')
admin.site.register(Category, CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_tag_path')
admin.site.register(Color, ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','marca', 'color', 'size', 'status', 'produto_em_destaque')
    list_editable = ('status','produto_em_destaque')
admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size', 'image_tag_path')
admin.site.register(ProductAttribute, ProductAttributeAdmin)