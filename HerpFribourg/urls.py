"""HerpFribourg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

from users.views import ProfilView, ProfilEditView
from herp.views import AmphibianListView, AmphibianDetailsView, ReptilesListView, ReptilesDetailsView
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('amphibiens/', AmphibianListView, name="amphibian_list"),
    path('amphibiens/<slug:slug>', AmphibianDetailsView, name="amphibian_details"),
    path('reptiles/', ReptilesListView, name="reptile_list"),
    path('reptiles/<slug:slug>', ReptilesDetailsView, name="reptiles_details"),
    path('accounts/profil/<int:pk>', login_required(ProfilView), name="profil"),
    path('accounts/profil/edit/<int:pk>', login_required(ProfilEditView), name="profil_update"),
    path('accounts/register/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)