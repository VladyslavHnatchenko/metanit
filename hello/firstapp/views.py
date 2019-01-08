from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect


def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    return render(request, "index.html", {"form": userform})

# def index(request):
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data["name"]
#             return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#         else:
#             return HttpResponse("Invalid data")
#     else:
#         userform = UserForm()
#         return render(request, "index.html", {"form": userform})

# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#     else:
#         userform = UserForm()
#         return render(request, "index.html", {"form": userform})

# def index(request):
#     userform = UserForm()
#     return render(request, "index.html", {"form": userform})

# def index(request):
#     header = "Personal Data"
#     langs = ["English", "German", "Spanish"]
#     user = {"name": "Tom", "age": 23}
#     addr = ("Apricot", 23, 45)
#
#     data = {
#         "header": header,
#         "langs": langs,
#         "user": user,
#         "address": addr
#     }
#
#     return render(request, "index.html", context=data)

# def index(request):
#     data = {
#         "header": "Hello Django",
#         "message": "Welcome to Python"
#     }
#     return render(request, "index.html", context=data)

# def index(request):
#     return render(request, "firstapp/home.html")

# def products(request, productid):
#     category = request.GET.get("cat", "")
#     output = "<h2>Product № {0} Category: {1}</h2>".format(productid, category)
#     return HttpResponse(output)
#
#
# def users(request):
#     id = request.GET.get("id", 1)
#     name = request.GET.get("name", "Tom")
#     output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
#     return HttpResponse(output)
#
#
# def index(request):
#     return HttpResponse("Index")
#
#
# def about(request):
#     return HttpResponse("About")
#
#
# def contact(request):
#     return HttpResponseRedirect("/about")
#
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")

# def products(request, productid=3):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)
#
#
# def users(request, id=1, name="Bob"):
#     output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
#     return HttpResponse(output)

# def products(request, productid=21):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)
#
#
# def users(request, id, name):
#     output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
#     return HttpResponse(output)
