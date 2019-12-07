from django.shortcuts import render
from .models import Pet2
# Create your views here.
def home(request):
	pet2 = Pet2.objects
	return render(request, 'home.html', {'pet2':pet2})