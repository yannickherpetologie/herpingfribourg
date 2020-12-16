from django.views.generic import ListView, DetailView

from .models import Herp

class AmphibianListView(ListView):
    model = Herp
    queryset = Herp.objects.all().filter(order__iexact='Amphibien').order_by('scientific_name')
    template_name = 'herp/list.html'

class AmphibianDetailsView(DetailView):
    queryset = Herp
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'herp/details.html'

class ReptilesListView(ListView):
    model = Herp
    queryset = Herp.objects.all().filter(order__iexact='Reptile').order_by('scientific_name')
    template_name = 'herp/list.html'

class ReptilesDetailsView():
    queryset = Herp
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'herp/details.html'