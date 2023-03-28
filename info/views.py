from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # form.save()
            Contact.objects.create(**form.cleaned_data)
        return render(request, 'contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', context={'form': form})

        