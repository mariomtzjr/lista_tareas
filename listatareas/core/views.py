from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class homePageView(TemplateView):
	template_name = "base.html"