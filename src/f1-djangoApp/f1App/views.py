from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("base2.html")
    context = {"latest_question_list": "woof"}
    return HttpResponse(template.render(context, request))


