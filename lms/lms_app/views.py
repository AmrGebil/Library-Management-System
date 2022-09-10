from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == "POST":
        add_Book=Bookform(request.POST,request.FILES)
        if add_Book.is_valid():
            add_Book.save()
        add_category=Categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    context={
        'category':Category.objects.all(),
       'books':Books.objects.all(),
        'bookform':Bookform(),
        'categoryform':Categoryform(),
        'allbooks': Books.objects.filter(active=True).count(),
        'avalilablebook': Books.objects.filter(status="available").count(),
        'soldbook': Books.objects.filter(status="sold").count(),
        'renterbook': Books.objects.filter(status="rental").count(),
         }
    return render(request,'pages/index.html',context)
def books(request):
    search=Books.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)
    context = {
        'category': Category.objects.all(),
        'books': search,
        'categoryform': Categoryform(),
    }

    return render(request,'pages/books.html',context)
def update(request,id):
    book_id=Books.objects.get(id=id)
    if request.method == "POST":
        book_save=Bookform(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = Bookform( instance=book_id)

    context={
        'updateform':book_save
    }
    return render(request,'pages/update.html',context)
def delete(request,id):
     book_delete=get_object_or_404(Books,id=id)
     if request.method == "POST":
          book_delete.delete()
          return  redirect('/')
     # context={
     #     'deletform':book_delete
     # }
     return render(request,'pages/delete.html')