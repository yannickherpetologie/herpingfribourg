from django.contrib import admin

from .models import Herp, HerpImage, Observation, SiteReproduction, PopulationSiteReproduction, Barrier, Stream

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

class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['object', 'name', 'type_object']}),
        ('Localisation', {'fields': ['commune', 'district', 'slug', 'gps', 'altitude', 'surface', 'surface_b']})
    ]

    prepopulated_fields = {'slug': ('object','district','commune'), }
    list_display = ('object', 'name', 'commune', 'district')

admin.site.register(SiteReproduction, SiteAdmin)

class BarrierAdmin(admin.ModelAdmin):
    fields = ['location', 'rte', 'slug', 't_length', 'nb_trap', 'date_begin', 'date_end']

    prepopulated_fields = {'slug': ('location',), }
    list_display = ('location', 't_length', 'nb_trap', 'date_begin', 'date_end')

admin.site.register(Barrier, BarrierAdmin)

class PopulationAdmin(admin.ModelAdmin):
    fields = [
        'site', 'herp', 'population_size'
    ]
    list_display = ('site', 'herp', 'population_size')
    search_filter = ['site',]

admin.site.register(PopulationSiteReproduction, PopulationAdmin)

class StreamAdmin(admin.ModelAdmin):
    fields = ['name', 'location', 'district', 'population_size']

    list_display = ('name', 'location', 'district', 'population_size')

admin.site.register(Stream, StreamAdmin)

"""
class ObservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['observer', 'date']}),
        ('Espèce', {'fields': ['herp', 'quantity', 'area', 'image']}),
    ]

    list_display = ('herp', 'observer', 'date', 'area')
    search_fields = ['herp', 'observer', 'date', 'area']

admin.site.register(Observation, ObservationAdmin)
"""