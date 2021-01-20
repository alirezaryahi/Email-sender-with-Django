from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactUs


# Create your views here.


def send_email(request):
    form = ContactForm(request.POST or None)
    success = ''
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            send_mail(name, request.user.email, message, ['alireza.rd69@gmail.com'])
            ContactUs.objects.create(name=name, email=email, message=message)
            success = 'Message has been sent'
            form = ContactForm()

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'home.html', context)
