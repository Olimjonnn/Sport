from django.shortcuts import render
from .models import *

def Index(request):
    main = Main.objects.all().order_by("-id")[0:3]
    con = {
        'main':main
    }
    return render(request, "index.html", con)

def News(request):
    return render(request, "news.html")

def Contact(request):
    return render(request, "contact.html")
