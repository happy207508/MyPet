from django.shortcuts import render

from .models import Pet
# Create your views here.
def allblogs(request):
	pets = Pet.objects
	return render(request, 'allblogs.html', {'pets':pets})