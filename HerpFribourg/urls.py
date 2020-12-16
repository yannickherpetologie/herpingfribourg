from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

from users.views import ProfilView, ProfilEditView
from herp.views import AmphibianListView, DetailsView, ReptilesListView, SiteListView
from .views import home, about

urlpatterns = [
    path('', home, name="home"),
    path('a-propos/', about, name="about"),
    path('sites/', SiteListView.as_view(), name='site_list'),
    path('amphibiens/', AmphibianListView.as_view(), name="amphibian_list"),
    path('amphibiens/<slug:slug>', DetailsView.as_view(), name="amphibian_details"),
    path('reptiles/', ReptilesListView.as_view(), name="reptile_list"),
    path('reptiles/<slug:slug>', DetailsView.as_view(), name="reptile_details"),
    path('accounts/profil/<int:pk>', login_required(ProfilView), name="profil"),
    path('accounts/profil/edit/<int:pk>', login_required(ProfilEditView), name="profil_update"),
    path('accounts/register/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)