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
        if request.method == "POST":
            # Method 01
            # name = int(request.POST["userName"])
            # fname = int(request.POST["fatherName"])

            # Method 02
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))

            data = {
                    "n1": num1,
                    "n2": num2,
                    "result": num1+num2
                    }
    
    except Exception as e:
        pass
    
    finally:
        return render (request, "userform.html", data)


