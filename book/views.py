from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.


def home(request):
    return render(request, 'store_book.html')


def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST, request.FILES)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('showbook')

    else:
        book = BookStoreForm()
    # book ta pathay dilam
    return render(request, 'store_book.html', {'form': book})


def show_books(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request, 'show_book.html', {'data': book})


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        info = BookStoreForm(request.POST, instance=book)
        if info.is_valid():
            info.save()
            return redirect('showbook')
    # ekhane form ta dekhar jonno   {'form': form}) eta use hoise
    return render(request, 'store_book.html', {'form': form})


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('showbook')
