from django.shortcuts import render
from graph.models import *

# Create your views here.
def index(request):
	context = 0
	return render(request, 'home.html', context)