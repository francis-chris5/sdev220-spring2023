from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from stuff.people import Person


townsfolk = [
    Person("Mary", 42, "Marysville"),
    Person("Henry", 12, "Henryville"),
    Person("Bradly", 38, "Borden")
    ]

def homePage(request):
    page = ""
    page += "<!DOCTYPE html><html><head><title>Tips and API example"
    page += "</title></head><body>"
    page += "<h2>Welcome</h2>"
    
    page += "<p><a href=\"contacts\">API</a> &nbsp; &nbsp; &nbsp;"
    page += "<a href=\"calculate\">Tip Calculator</a> &nbsp; &nbsp; &nbsp;"
    page += "<a href=\"template\">Basic Template</a></p>"
    
    page += "</body></html>"
    
    return HttpResponse(page)


def basicTemplate(request):
    return render(request, "basic.html", {"title": "Template Page", "message": "hello dynamic world"})


def calculateTip(request):
    return render(request, "tipInput.html")


def displayTip(request):
    price = float(request.GET["price"])
    service = float(request.GET["service"])
    print(price, service)
    service /= 100
    tipAmount = price * service
    return render(request, "tipResponse.html", {"title": "Tip Today", "tipAmount": format(tipAmount, ".2f")})



def simpleAPI(request):
    data = ""
    for t in townsfolk:
        data += str(t) + "<br>"
    return HttpResponse(data)




















#####################################
