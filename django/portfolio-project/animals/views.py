from django.shortcuts import render

# Create your views here.

def pet(request):
	return render(request,'portfolio-2-col.html')