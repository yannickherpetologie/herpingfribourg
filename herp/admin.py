from django.contrib import admin

from .models import Herp, HerpImage, Observation

class HerpImageInline(admin.StackedInline):
    model = HerpImage
    extra = 1

class HerpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['order', 'scientific_name', 'common_name', 'author', 'slug']}),
        ('Status de conservation', {'fields': ['iucn_status']}),
        ('Détails', {'fields': ['description']})
    ]

    prepopulated_fields = {'slug': ('scientific_name',), }
    inlines = [HerpImageInline]

    list_display = ('scientific_name', 'common_name', 'order', 'iucn_status')
    search_fields = ['scientific_name', 'common_name', 'order']
    search_filter = ('order',)

admin.site.register(Herp, HerpAdmin)

class ObservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['observer', 'date']}),
        ('Espèce', {'fields': ['herp', 'details', 'image']}),
    ]

    list_display = ('herp', 'observer', 'date')
    search_fields = ['herp', 'observer', 'date']

admin.site.register(Observation, ObservationAdmin)
