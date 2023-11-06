from django.shortcuts import render, redirect
from store.models import Product
from store.models import Category
from django.views import View


# Create your views here.

class Index(View):
    def get(self, request):
        all_products = None
        all_categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            all_products = Product.get_all_product_by_id(categoryID)
        else:
            all_products = Product.get_all_products()

        data = {
            'products': all_products,
            'categories': all_categories,
        }
        print(request.session.get('email'))
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = 1 + quantity
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request)
        return redirect('home')
