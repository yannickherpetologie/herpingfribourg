from django.views.generic import ListView, DetailView

from .models import Herp, Site


class SiteListView(ListView):
    model = Site
    queryset = Site.objects.order_by('district', 'commune')
    template_name = 'herp/site_list.html'
    context_object_name = 'sites'

class AmphibianListView(ListView):
    model = Herp
    queryset = Herp.objects.filter(order='A').order_by('scientific_name')
    template_name = 'herp/list.html'
    context_object_name = 'herps'

class DetailsView(DetailView):
    model = Herp
    slug_field = 'slug'
    template_name = 'herp/details.html'

class ReptilesListView(ListView):
    model = Herp
    queryset = Herp.objects.filter(order='R').order_by('scientific_name')
    template_name = 'herp/list.html'
    context_object_name = 'herps'