from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
#django will read the templates folder to look for the index
#create a template html for every view function you have. should be the same name

def index(request):
    all_products=Product.objects.all()
    return render(request,'index.html',{'products':all_products})

# the dictionatary above provides data to be used in the template. IT IS called the context
# step 1 : load data in view function
# step 2: provide data to be used in the template to the render function
# step 3: work on the data in the template file

def list_items(request):
    return render(request,'list_items.html')

def email(request):
    return render(request,'email.html')

def phone(request):
    return render(request,'phone.html')

def office_address(request):
    return render(request,'office_address.html')

def about_us(request):
    return render(request,'about_us.html')

# Create your views here.

