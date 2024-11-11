# django-admin startproject <project_name>
# python manage.py runserver 4444
# python manage.py startapp
# python manage.py migrate

from django.http import HttpResponse   # only send text message
from django.shortcuts import render # send html file


def aboutUs(request):
    message = """
    <center>
        <h1>
            <font color="red">
                <i>Hi..., </i></br>
                <b><u>Er. Arjun Prajapati.</u></b>
            </font>
        </h1>
    </center>
    """
    return HttpResponse(message)

# dynamic routes
# int, string, slug(hello-ws-iip)
def course(request, course_id):
    message = ''
    if course_id == 1:
        message = "Python"
    elif course_id == 2:
        message =  "C Programming"
    elif course_id == 3:
        message =  "C++ Programming"
    elif course_id == 4:
        message =  "Java Programming"
    elif course_id == 5:
        message =  "R Programming"
    elif course_id == 6:
        message =  "DSA Programming"
    else:
        message = "No a course."
    
    return HttpResponse(message)

# render a html page.
def homePage(request):
    return render (request, "index.html")


def aboutUsPage(request):
    return render(request, 'aboutus.html')

