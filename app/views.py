from django.shortcuts import render, HttpResponse
from .models import Agency

# Create your views here.
def home(request):
    return render(request, "home.html", {"agencies": Agency.objects.all()})