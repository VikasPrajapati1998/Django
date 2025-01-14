from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


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
        data = {}
        
        if request.method == "POST":
            # Method 01
            # num1 = int(request.POST["num1"])
            # num2 = int(request.POST["num2"])

            # Method 02
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))
            num3 = num1 + num2

            data = {
                    "n1": num1,
                    "n2": num2,
                    "result": num3
                    }
            
            urls = "thanks?output={}".format(num3)
            return HttpResponseRedirect(urls)
        
            # return redirect("thanks")
    
    except Exception as e:
        pass
    
    return render (request, "userform.html", data)

def thanks(request):
    value = 0
    if request.method == "GET":
        value = request.GET.get("output")
    context = {'output': value}
    return render(request, 'thanks.html', context)


def submitform(request):
    try:
        data = {}
        if request.method == "POST":
            # Method 02
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))
            num3 = num1 + num2

            data = {
                    "n1": num1,
                    "n2": num2,
                    "result": num3
                    }
            
            
            return HttpResponse(num3)
    
    except Exception as e:
        pass

