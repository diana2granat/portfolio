from django.shortcuts import render

def about_view(request):
    return render (request,'about.html')

def education_view(request):
    return render (request,'education.html')

def projects_view(request):
    return render (request,'projects.html')

def moreinfo_view(request):
    return render (request,'moreinfo.html')

def contact_view(request):
    return render (request,'contact.html')