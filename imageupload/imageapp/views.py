from django.shortcuts import render
from .models import Image
#for forms 
from .forms import ImageForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    #for data get
    img = Image.objects.all()
    context = {'form':form,'img':img}
    return render(request, 'myapp/image.html', context)