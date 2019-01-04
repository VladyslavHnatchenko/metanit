from django.shortcuts import render
from django.http import HttpResponse


def products(request, productid=3):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=1, name="Bob"):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)

# def products(request, productid=21):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)
#
#
# def users(request, id, name):
#     output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
#     return HttpResponse(output)


def index(request):
    return HttpResponse("<h2>Main page</h2>")


def about(request):
    return HttpResponse("<h2>About site</h2>")


def contact(request):
    return HttpResponse("<h2>Contacts</h2>")
