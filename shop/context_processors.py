from django.shortcuts import get_object_or_404

from .models import Category, Subcategory


def menu_categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return {'menu_categories': categories, 'subcategories': subcategories}
