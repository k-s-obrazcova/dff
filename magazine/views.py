from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'magazine/index.html')

def supplier_list(request):
    list_supplier = Supplier.objects.filter(logical_del=True)
    context = {
        'list_sup': list_supplier
    }
    return render(request, 'magazine/supplier/catalog.html', context)

def supplier_details(request, id):
    supplier = get_object_or_404(Supplier, pk = id)

    context = {
        'supplier_object': supplier
    }
    return render(request, 'magazine/supplier/details.html', context)
def supplier_create(request):
    if request.method == "POST":
        form_supplier = SupplierForm(request.POST)
        if form_supplier.is_valid():
            new_supplier = Supplier(**form_supplier.cleaned_data)
            new_supplier.save()
            messages.success(request, 'Поставщик успешно добавлен')
            return redirect('catalog_supplier_page')
        messages.error(request, 'Неверно заполнены поля')
    else:
        form_supplier = SupplierForm()
    context = {
        'form': form_supplier
    }
    return render(request, 'magazine/supplier/create.html', context)

def product_list(request):
    list_product = Product.objects.filter(exists=True)
    context = {
        'list_product': list_product
    }
    return render(request, 'magazine/product/catalog.html', context)


#________________________________________________________________________

from django.contrib.auth import login, logout
from  django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm, LoginForm

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            login(request, user)

            messages.success(request, 'Вы успешно зарегистрировались')

            return redirect('home_page')

        messages.error(request, 'Что-то пошло не так')
    else:
        form = RegistrationForm()

    return render(request, 'magazine/auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            print('is_anon: ', request.user.is_anonymous)
            print('is_auth: ', request.user.is_authenticated)

            login(request, user)

            print('is_anon: ', request.user.is_anonymous)
            print('is_auth: ', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизовались')

            return redirect('home_page')
        messages.error(request, 'Что-то пошло не так')
    else:
        form = LoginForm()

    return render(request,'magazine/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)

    messages.warning(request, 'Вы вышли из аккаунта!')
    return redirect('log in')


def anon(request):
    print('is_active: ', request.user.is_active)
    print('is_anonymous: ', request.user.is_anonymous)
    print('is_authenticated: ', request.user.is_authenticated)
    print('is_staff: ', request.user.is_staff)
    print('is_superuser: ', request.user.is_superuser)

    print('может добавлять поставщика? ', request.user.has_perm('magazine.add_supplier'))
    print('может добавлять и изменять поставщика? ', request.user.has_perms(['magazine.add_supplier', 'magazine.change_supplier']))
    print('может изменять адрес?', request.user.has_perm('magazine.change_address'))
    return render(request, 'magazine/test/anon.html')

@login_required()
def auth(request):
    return render(request, 'magazine/test/auth.html')

@permission_required('magazine.add_supplier')
def can_add_supplier(request):
    return render(request, 'magazine/test/can_add_supplier.html')

@permission_required(['magazine.add_supplier', 'magazine.change_supplier'])
def can_add_change_supplier(request):
    return render(request, 'magazine/test/can_add_change_supplier.html')

@permission_required('magazine.change_address')
def can_change_address(request):
    return render(request,'magazine/test/change_address.html')