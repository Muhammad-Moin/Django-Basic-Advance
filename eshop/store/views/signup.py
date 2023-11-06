from django.shortcuts import render, redirect
from store.models.customer import Customer
import re
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def validateUser(self, customer):
        error_message = None
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (not customer.first_name):
            error_message = 'First Name required!'

        elif (len(customer.first_name) < 3):
            error_message = 'First Name length must be greater than 5'

        elif (not customer.last_name):
            error_message = 'Last Name required!'

        elif (len(customer.last_name) < 3):
            error_message = 'Last Name length must be greater than 5'

        elif not customer.phone:
            error_message = 'Phone number required!'

        elif (len(customer.phone) < 8):
            error_message = 'Please use correct phone number'
        elif not customer.email:
            error_message = 'Email required!'

        elif not customer.password:
            error_message = 'Password required!'
        elif (len(customer.password) < 8):
            error_message = 'Password length must be 8 or greater'
        else:
            if (re.fullmatch(regex, customer.email)):
                error_message = None
                if customer.isExits():
                    error_message = 'Email address is already exits'
            else:
                error_message = 'Email is invalid!'
        return error_message

    def registerUser(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = Signup.validateUser(self, customer)
        userFillData = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'password': password,
        }

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': userFillData
            }
            return render(request, 'signup.html', data)

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        return self.registerUser(request)
