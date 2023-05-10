from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
 

def cv(request):
	template = loader.get_template("cv.html")
	return HttpResponse(template.render())
	#return render(request, "show.html")
