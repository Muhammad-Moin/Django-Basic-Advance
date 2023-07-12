from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print('this is customer', customer)

        loginFillData = {
            'email': email,
            'password': password
        }

        error_message = None
        if not email:
            error_message = 'Email Required!'
        elif not password:
            error_message = 'Password Required!'
        else:
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer_id'] = customer.id
                    request.session['email'] = customer.email
                    return redirect('home')
                else:
                    error_message = 'Password Invalid!'
            else:
                error_message = 'Email not found please signup'
        data = {
            'error': error_message,
            'values': loginFillData,
        }
        return render(request, 'login.html', data)
def logout(request):
    request.session.clear()
    return redirect('login')