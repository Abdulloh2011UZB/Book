from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Category, Book


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    return render(request, 'book_delete.html', {'book': book})


def category_books(request, id):
    category = Category.objects.get(id=id)
    books = Book.objects.filter(category_id=id)

    return render(request, 'category_book.html', {
        'category': category,
        'books': books
    })