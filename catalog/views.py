from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from .models import Clothes,Clothes_name,Firma


def index(request):

    num_clothes = Clothes.objects.all().count()
    num_clname = Clothes_name.objects.all().count()

    #num__cl = Clothes_name.objects.filter(status__exact='a').count()
    num_firma =Firma.objects.count()


    return render(
        request,
        'index.html',
        context={'num_clothes': num_clothes, 'num_clname': num_clname,
                  'num_firma': num_firma},
    )

from django.views import generic

class ClothesListView(generic.ListView):
    model = Clothes
    paginate_by = 2
class ClothesDetailView(generic.DetailView):
    model = Clothes
from django.views import generic

class FirmaListView(generic.ListView):
    model = Firma
class FirmaDetailView(generic.DetailView):
    model = Firma
    model2=Clothes
    paginate_by = 2
