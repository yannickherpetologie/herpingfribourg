from django.shortcuts import render
from herp.models import Herp

#from users.forms import SignUpForm

def home(request):
    herps = Herp.objects.all().order_by('order', 'scientific_name')
    return render(request, 'herpfribourg/home.html', {'herps': herps})

def about(request):
    return render(request, 'herpfribourg/a-propos.html')

def legislation(request):
    return render(request, 'herpfribourg/legislation.html')