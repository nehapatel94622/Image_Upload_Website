from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.
def Home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = ImageModel.objects.all()
    return render(request, 'home.html', {'img':img, 'form':form})