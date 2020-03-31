from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
        if request.method == 'POST':
            if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
                product = Product()
                product.title = request.POST['title']
                product.body = request.POST['body']
                if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                    product.url = request.POST['url'] #then leave it alone
                else:
                    product.url = request.POST['url'] + request.POST['url']
                product.icon = request.FILES['icon']
                product.image = request.FILES['icon']
                product.pub_date = timezone.datetime.now()
                product.hunter = request.user
                product.save() #actually inserts this into the database
                return redirect('/products/' + str(product.id)) ##sends it back to urls.py w/ PRODUCT ID
            else:
                return render(request, 'products/create.html', {'error':'You must complete the form'})
        else:
            return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})
