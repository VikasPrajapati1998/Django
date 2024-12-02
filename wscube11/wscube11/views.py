from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def service(request):
    return render (request, "service.html")

def contact(request):
    return render (request, "contact.html")

def userForm(request):
    try:
        # Method 01
        # name = request.GET["userName"]
        # fname = request.GET["fatherName"]

        # Method 02
        name = request.GET.get("userName")
        fname = request.GET.get("fatherName")

        print(f"Name: {name}") 
        print(f"Father Name: {fname}.")
    
    except Exception as e:
        pass
    
    finally:
        return render (request, "userform.html")


