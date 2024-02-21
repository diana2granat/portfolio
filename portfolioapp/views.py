from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def about_view(request):
    return render (request,'about.html')

def education_view(request):
    return render (request,'education.html')

def projects_view(request):
    return render (request,'projects.html')

def moreinfo_view(request):
    return render (request,'moreinfo.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'diana2granat@gmail.com', [recipient])
            # Redirect to a success page or whatever you want
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})