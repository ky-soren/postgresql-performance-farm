from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"response-code": 200}
    return render(request, "index.html", context)