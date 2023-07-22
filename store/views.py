from django.shortcuts import render

def home(request):
    return render(request,'home-04.html')

def about(request):
    return render(request,'about-us-01.html', )

def blog(request):
    return render(request,'blog-layout-02.html')

def checkout(request):
    return render(request,'checkout.html')


def blog_detail(request):
    return render(request,'blog-post-01.html')

def cart(request):
    return render(request,'cart.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faqs.html')

def login_register(request):
    return render(request,'login-register.html')

def product_detail(request):
    return render(request,'product-page-09.html')

def shop(request):
    return render(request,'shop-page-08.html')

def favorites(request):
    return render(request,'wishlist.html')

# Create your views here.
