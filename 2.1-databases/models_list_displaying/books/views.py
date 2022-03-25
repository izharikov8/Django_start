from django.shortcuts import render, redirect
from books.models import Book


def books_view(request):
    all_books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': all_books
    }
    return render(request, template, context)


def one_book(request, pub_date):
    book = Book.objects.get(pub_date=pub_date)
    print(book)
    sort_list = list(Book.objects.all().order_by('pub_date'))
    print(sort_list)
    prev_book = sort_list[sort_list.index(book)-1]
    print(prev_book)
    next_book = sort_list[sort_list.index(book)+1]
    print(next_book)
    template = 'books/one_book.html'
    context = {
        'book': book,
        'prev': prev_book,
        'next': next_book
    }
    return render(request, template, context)



