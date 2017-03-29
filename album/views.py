from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView

def first_view(request):
	return HttpResponse('<h1> esta es mi primer vista en Django</h1>')

class PhotoListView(ListView):
	model=Photo 
class PhotoDetailView(DetailView):
	model=Photo




def category(request):
	category_list=Category.objects.all()
	context={'object_list': category_list}
	return render(request, 'album/category.html', context)


def category_detail(request, category_id):
	category=Category.objects.get(id=category_id)
	context={'object': category}
	return render(request, 'album/category_detail.html', context)	