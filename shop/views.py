import json
from decimal import Decimal as D
from django.db.models import Max, Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from shop.models import Shopproduct, Category, Subcategory, Contactform


def index(request):
    indproducts = Shopproduct.objects.all()
    return render(request, 'index.html', {'indproducts': indproducts})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phoneno']
        msg = request.POST['msg']

        contactdata = Contactform(person_name=name, person_email=email, person_phone=phone, person_msg=msg)
        contactdata.save()

        context = {
            'rep': 'we will contact you soon'
        }

        return render(request, 'contact.html', context)

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def checkout(request):
    return render(request, 'checkout.html')


def singleproduct(request, single_prod):
    single_prod = str(single_prod)
    singleprod = Shopproduct.objects.get(slug=single_prod)

    context = {'singleprod': singleprod}
    return render(request, 'single.html', context)


def allproducts(request):
    products = Shopproduct.objects.all()[:3]
    products2 = Shopproduct.objects.all()[3:]

    context = {'products': products,
               'products2': products2,
               'category': ''
               }

    if 'min' in request.GET:
        filter_price1 = request.GET.get('min')
        filter_price2 = request.GET.get('max')
        print(type(filter_price1))
        print(filter_price2)

        if filter_price1 == '':
            filter_price1 = 0
        if filter_price2 == '':
            filter_price2 = Shopproduct.objects.all().aggregate(Max('product_price'))

        filter_price1 = float(filter_price1)
        filter_price2 = float(filter_price2)

        products = Shopproduct.objects.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[:3]
        products2 = Shopproduct.objects.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[3:]

        print('success')

        context = {"products": products, "products2": products2, }
        return render(request, 'products.html', context)

    return render(request, 'products.html', context)


def categoryproducts(request, cat):
    cat = str(cat)
    prodcatmain = get_object_or_404(Category, slug=cat)

    products = prodcatmain.products.all()[:3]
    products2 = prodcatmain.products.all()[3:]

    context = {'products': products,
               'products2': products2,
               'category': prodcatmain,
               }

    if 'min' in request.GET:
        filter_price1 = request.GET.get('min')
        filter_price2 = request.GET.get('max')
        print(type(filter_price1))
        print(filter_price2)

        if filter_price1 == '':
            filter_price1 = 0
        if filter_price2 == '':
            filter_price2 = Shopproduct.objects.all().aggregate(Max('product_price'))

        filter_price1 = float(filter_price1)
        filter_price2 = float(filter_price2)

        products = prodcatmain.products.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[:3]
        products2 = prodcatmain.products.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[3:]

        print('success')

        context = {"products": products,
                   "products2": products2,
                   'category': prodcatmain
                   }
        return render(request, 'products.html', context)

    return render(request, 'products.html', context)


def productscatsub(request, cat, catsub):
    catsub = str(catsub)
    prodsubcat = get_object_or_404(Subcategory, slug=catsub)
    products = prodsubcat.subproducts.all()[:3]
    products2 = prodsubcat.subproducts.all()[3:]

    category = get_object_or_404(Category, slug=cat)
    context = {
        'products': products,
        'products2': products2,
        'category': category,
        'prodsubcategory': prodsubcat
    }

    if 'min' in request.GET:
        filter_price1 = request.GET.get('min')
        filter_price2 = request.GET.get('max')
        print(type(filter_price1))
        print(filter_price2)

        if filter_price1 == '':
            filter_price1 = 0
        if filter_price2 == '':
            filter_price2 = Shopproduct.objects.all().aggregate(Max('product_price'))

        filter_price1 = float(filter_price1)
        filter_price2 = float(filter_price2)

        products = prodsubcat.subproducts.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[:3]
        products2 = prodsubcat.subproducts.filter(product_price__gte=filter_price1).filter(
            product_price__lte=filter_price2).order_by('product_price')[3:]

        context = {
            "products": products,
            "products2": products2,
            'category': category,
            'prodsubcategory': prodsubcat
        }
        return render(request, 'products.html', context)

    return render(request, 'products.html', context)


def searchproduct(request):
    query = request.GET['query']
    query_cat = request.GET['search_category']
    print(query, query_cat)
    query_cat = str(query_cat)

    if query_cat == 'Allproducts':
        products = Shopproduct.objects.filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))[:3]
        products2 = Shopproduct.objects.filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))[3:]

        context = {'products': products,
                   'products2': products2,
                   'category': ''
                   }
        return render(request, 'products.html', context)
    else:
        prodcatmain = get_object_or_404(Category, slug=query_cat)

        products = prodcatmain.products.filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))[:3]
        products2 = prodcatmain.products.filter(Q(product_name__icontains=query) | Q(product_desc__icontains=query))[3:]

        context = {'products': products,
                   'products2': products2,
                   'category': prodcatmain,
                   }

        return render(request, 'products.html', context)
