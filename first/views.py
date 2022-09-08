from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader, Template


def hello_world(request: HttpRequest) -> HttpResponse:
	template: Template = loader.get_template("first.html")
	return HttpResponse(template.render())
