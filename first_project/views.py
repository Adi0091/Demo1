from django.http import HttpResponse
from django.shortcuts import render
from .form import userForm

def home(request):
    # data={
    #     'title': "Home",
    #     'name': "Aditya",
    #     'list1': ['PHP', 'JAVA', 'Python', 'Django'],
    #     'num' : [10, 20, 30 ,40 ,50],
    #     'list': [
    #             {'first': "adi",'last':'waghaye'},
    #              {'first':'Seema','last': 'Tumsare'}
    #              ]
    # }
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    fn=userForm()
    data = {'form':fn}

    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            data = {
                'form':fn,
                'output'
            }

    return render(request, "contact.html")

def course(request):
    return HttpResponse("this is course page.")

def courseDetail(request, courseid):
    return HttpResponse(courseid)