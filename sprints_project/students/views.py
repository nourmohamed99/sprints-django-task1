from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def Welcome(request):
	 return HttpResponse("welcome to our site")


def Show(request):
	template = loader.get_template("show.html")
	return HttpResponse(template.render())
	#return render(request, "show.html")
