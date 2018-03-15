from django.contrib import admin


from .models import Firma,Clothes,Clothes_name

#admin.site.register(Firma)
#admin.site.register(Clothes)
#admin.site.register(Clothes_name)

class Firma_nameInline(admin.TabularInline):
    model = Clothes


class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_name', 'date_of_creation')
    inlines = [Firma_nameInline]
    fields = ['firma_name', ('date_of_creation')]
admin.site.register(Firma, FirmaAdmin)

class Clothes_nameInline(admin.TabularInline):
    model =Clothes_name

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('clothes','firma')
    inlines = [Clothes_nameInline]

@admin.register(Clothes_name )
class Clothes_nameAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('clothes', 'imprint', 'id')
        }),
        ('Satylymda', {
            'fields': ('status', 'due_back')
        }),
    )