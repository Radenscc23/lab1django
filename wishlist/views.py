from django.shortcuts import render

def show_wishlist(request):
    return render(request, "wishlist.html")
    
# Create your views here.
