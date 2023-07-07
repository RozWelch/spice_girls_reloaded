from django.shortcuts import render
from .models import Spices


def all_spices(request):
    """ A view to show all products, including sorting and search queries """

    spices = Spices.objects.all()

    context = {
        'spices': spices,
    }

    return render(request, 'products/products.html', context)
