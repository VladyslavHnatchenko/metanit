from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import HttpResponsePermanentRedirect
from .models import Person
from .models import Company, Product
from .models import Course, Student, User, Account


sam = User.objects.create(name="Sam")

acc = Account.objects.create(login="1234", password="6565", user=sam)

acc.user.name = "Bob"
acc.user.save()

# python = Course.objects.create(name="Python")
# python.student_set.create(name="Bob")
#
# sam = Student(name="Sam")
# sam.save()
# python.student_set.add(sam)

# tom = Student.objects.create(name="Tom")
# tom.courses.create(name="Algebra")
#
# courses = Student.objects.get(name="Tom").courses.all()
#
# studes = Student.objects.filter(courses__name="Algebra")
#
# apple = Company.objects.create(name="Apple")
# apple.product_set.create(name="iPhone 8", price=67890)
#
# ipad = Product(name="iPad", price=34560)
# apple.product_set.add(ipad, bulk=False)


"""get data from DB"""


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


"""save data in DB"""


def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")


"""edit data in DB"""


def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})

    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


"""delete data from DB"""


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# def create(request):
#     if request.method == "POST":
#         tom = Person()
#         tom.name = request.POST.get("name")
#         tom.age = request.POST.get("age")
#         tom.save()
#     return HttpResponseRedirect("/")

# def index(request):
#     userform = UserForm()
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data["name"]
#             return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#     return render(request, "index.html", {"form": userform})

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
