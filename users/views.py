from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm

class SignUpView(CreateView):
    model = get_user_model()
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfilView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'registration/profil.html'
    context_object_name = 'profil'

class ProfilEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'email', 'phone', 'avatar']
    template_name = 'registration/profil_edit.html'

    def get_success_url(self):
        return reverse('profil', kwargs={'pk': self.request.user.pk})