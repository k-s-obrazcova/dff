from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . import models as m

def home(request):
    return HttpResponse("<h1>Добро пожаловать</h1>")

def all_books(request):
    books = m.Books.objects.all()
    page = "<h1>Книги: </h1>"

    for book in books:
        page += f"<a href='/lib/books/{book.id}'>{book.name}</p>"
    return HttpResponse(page)

def id_book(request, id):
    book = get_object_or_404(m.Books, pk=id)

    page = f'''
    <div style="background-color: #efbeff; padding: 20px; margin: 0 auto; width:500px;">
    <h1 style="text-align: center;">Книгa: </h1>
    <div style = "margin-bottom: 10px;">
        <strong> Название книги: </strong> {book.name} 
    </div>
    <div style = "margin-bottom: 10px;">
        <strong> Описание: </strong> {book.description} 
    </div>
        <div style = "margin-bottom: 10px;">
        <strong> Цена: </strong> {book.price} 
    </div>
        <div style = "margin-bottom: 10px;">
        <strong> Количество страниц в книге: </strong> {book.count_pages} 
    </div>
    '''

    return HttpResponse(page)


def name_book(request, name):
    books = m.Books.objects.filter(name__contains=name)
    page = "<h1>Книги по имени: </h1>"

    for book in books:
        page += f"<a href='/lib/books/{book.id}'>{book.name}</p>"
    return HttpResponse(page)

def info(request):
    return render(request, 'library/index.html')

def get_all_book(request):
    books = m.Books.objects.all()
    context = {
        'list': books
    }
    return render(request, 'library/query_all.html',context=context)

def get_one_book(request, id):
    book = get_object_or_404(m.Books, pk=id)
    return render(request, 'library/query_get.html', {'one_book': book})

def get_one_filter_book(request):
    find_books= m.Books.objects.filter(exists=request.GET.get('is_ex'))
    return render(request,'library/query_filter.html', {'filter_books': find_books})

def get_more_filter_book(request):
    find_books = m.Books.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    return render(request, 'library/query_filter.html', {'filter_books': find_books})

def get_one_by_one_filter_book(request):
    find_books = m.Books.objects.filter(price__lte=request.GET.get('max_price'))
    find_books = find_books.filter(name__contains=request.GET.get('name'))

    return render(request,'library/query_filter.html', {'filter_books': find_books})

def create_blank_book(request):
    new_book = m.Books()
    new_book.price = 10
    new_book.save()
    return render(request, 'library/message.html', context={'message': 'Пустая книга успешно создана'})

def create_book(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    count_pages = request.GET.get('count_pages')

    new_book = m.Books()
    new_book.name = name
    new_book.price = price
    new_book.count_pages = count_pages

    new_book.save()
    return render(request, 'library/message.html', context={'message': 'Книга с указанными данными создана'})

def update_book(request, id):
    upd_book = get_object_or_404(m.Books, pk=id)

    upd_book.price=1000

    upd_book.save()
    return render(request, 'library/message.html', context={'message': f'Книга с ID {upd_book.pk} была успешно изменена'})