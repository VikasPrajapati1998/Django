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
    data = {}
    try:
        if request.method=="GET":
            # Method 01
            # name = int(request.GET["userName"])
            # fname = int(request.GET["fatherName"])

            # Method 02
            n1 = int(request.GET.get("num1"))
            n2 = int(request.GET.get("num2"))

            data = {
                    "n1": n1,
                    "n2": n2,
                    "result": n1 + n2
                    }
    
    except Exception as e:
        pass
    
    finally:
        return render (request, "userform.html", data)

