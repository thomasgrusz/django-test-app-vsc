import re

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime

# def home(request):
#     return HttpResponse("Hello Mindcode!")


# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%a, %d %b, %Y at %X")

#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "<h1>Hello there, " + clean_name + "!</h1> It's " + formatted_now
#     return HttpResponse(content)

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def home(request):
    return render(request, "hello/home.html")


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")
