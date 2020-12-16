from django.contrib import admin

from .models import Herp, HerpImage, Observation, Site, Population

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['object', 'name']}),
        ('Localisation', {'fields': ['commune', 'district', 'slug', 'gps', 'altitude', 'surface']})
    ]

    prepopulated_fields = {'slug': ('object','district','commune'), }
    list_display = ('object', 'name', 'commune', 'district')

admin.site.register(Site, SiteAdmin)

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


class PopulationAdmin(admin.ModelAdmin):
    fields = [
        'site', 'herp', 'population_size'
    ]
    list_display = ('site', 'herp', 'population_size')
    search_filter = ['site',]

admin.site.register(Population, PopulationAdmin)


class ObservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['observer', 'date']}),
        ('Espèce', {'fields': ['herp', 'quantity', 'area', 'image']}),
    ]

    list_display = ('herp', 'observer', 'date', 'area')
    search_fields = ['herp', 'observer', 'date', 'area']

admin.site.register(Observation, ObservationAdmin)
