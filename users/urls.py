from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SignUpView, ProfilView

urlpatterns = [
    path('', SignUpView.as_view(), name="signup")
]