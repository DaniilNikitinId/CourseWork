from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.db.models import Q
from django.http import HttpRequest
# from store.forms import FilterCatType
from store.models import Store, Category, TagPost, Brand, Age, TypeFeed,Size

# from store.forms import AddPostForm, UploadFileForm
# from store.models import Women, Category, TagPost, UploadFiles
# from django.views import View
#
# from store.utils import DataMixin

mypath = ''




def getBrand():
    allBrand = Brand.objects.all()
    return allBrand

def getAge():
    allAge = Age.objects.all()
    return allAge

def getTypeFeed():
    allTypeFeed = TypeFeed.objects.all()
    return allTypeFeed

def getCategory():
    allCategory = Category.objects.all()
    return allCategory

def getSize():
    allSize = Size.objects.all()
    return allSize

def getDiets():
    diets = [
        'Повседневный корм',
        'Диеты'
    ]
    return diets


def index(request):
    """"Главная страница"""
    vet = Store.published.filter(Q(tags__tag='собаки диеты') | Q(tags__tag='кршки диеты'))
    puppies = Store.published.filter(Q(tags__tag='собаки щенки')| Q(tags__tag='кошки котята'))
    data = {
        'posts': vet,
        'puppies': puppies,
    }
    print(puppies)
    return render(request, 'store/index.html', data)


def cats(request):
    posts = Store.published.filter(cat2__name='кошки')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'allCategory': getCategory(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed()
    }
    print(posts)
    return render(request, 'store/cats.html', data)

#CatsSterilized
def CatsSterilized(request):
    posts = Store.published.filter(cat2__name='кошки', tags__tag='кошки стерилизованные')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed()
    }
    return render(request, 'store/cats.html', data)


def kittens(request):
    posts = Store.published.filter(cat2__name='кошки', tags__tag='кошки котята')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed()
    }
    return render(request, 'store/cats.html', data)


def dietsCats(request: HttpRequest):
    global mypath
    mypath = request.path
    posts = Store.published.filter(cat2__name='кошки', tags__tag='кошки диеты')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),

    }
    return render(request, 'store/cats.html', data)


def dogs(request):
    posts = Store.published.filter(cat2__name='собаки')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize':getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)



def bigDogs(request):
    posts = Store.published.filter(cat2__name='собаки', tags__tag='собаки крупные породы')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)

def mediumDogs(request):
    posts = Store.published.filter(cat2__name='собаки', tags__tag='собаки средние породы')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)

def smallDogs(request):
    posts = Store.published.filter(cat2__name='собаки', tags__tag='собаки мелкие породы')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)

def dietsDogs(request):
    posts = Store.published.filter(cat2__name='собаки', tags__tag='собаки диеты')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)


def puppies(request):
    posts = Store.published.filter(cat2__name='собаки', tags__tag='собаки щенки')
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)

def filterCats(request):
    """"Фильтрация товара (радио)"""
    typeFeed = request.GET.get('typeFeed')
    age = request.GET.get('age')
    brand = request.GET.get('brand')
    print(typeFeed, age, brand)
    posts = Store.published.filter(cat2__name='кошки')

    if typeFeed:
        posts = posts.filter(typeFeed__name=typeFeed)
    if age:
        posts = posts.filter(age__name=age)
    if brand:
        posts = posts.filter(brand__name=brand)

    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed()
    }

    return render(request, 'store/cats.html', data)

def filterDogs(request):
    """"Фильтрация товара (радио)"""
    typeFeed = request.GET.get('typeFeed')
    age = request.GET.get('age')
    brand = request.GET.get('brand')
    size = request.GET.get('size')
    diets = request.GET.get('diets')
    print(typeFeed, age, brand,size,diets)
    posts = Store.published.filter(cat2__name='собаки')

    if typeFeed:
        posts = posts.filter(typeFeed__name=typeFeed)
        print('typeFeed',posts)
    if age:
        posts = posts.filter(age__name=age)
        print('age',posts)
    if brand:
        posts = posts.filter(brand__name=brand)
        print('brand',posts)
    if size:
        posts = posts.filter(size__name=size)
        print('size',posts)
    if diets:
        posts = posts.filter(tags__tag='собаки диеты')
        print('diets', diets)
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    return render(request, 'store/dogs.html', data)
def searchCats(request):
    """"поиск по лупе"""
    posts = Store.published.filter(cat2__name="кошки")
    search_term = request.GET.get('searchCats', None)
    print('search_term',search_term)
    if search_term:
        posts = posts.filter(
            Q(article__icontains=search_term) |
            Q(title__icontains=search_term) |
            Q(content__icontains=search_term) &
            Q(cat2__name="кошки")
        ).distinct()
    data = {
        'posts': posts,
    }
    print('posts', posts)
    return render(request, 'store/cats.html', data)


def searchDogs(request):
    """"поиск по лупе"""
    posts = Store.published.filter(cat2__name="собаки")
    search_term = request.GET.get('searchDogs', None)
    print('==-=search_term', search_term)
    if search_term:
        posts = posts.filter(
            Q(article__icontains=search_term) |
            Q(title__icontains=search_term) |
            Q(tags__tag__icontains=search_term) |
            Q(content__icontains=search_term)
        ).distinct()
    data = {
        'posts': posts,
        'allBrand': getBrand(),
        'getAge': getAge(),
        'getTypeFeed': getTypeFeed(),
        'getSize': getSize(),
        'getDiets': getDiets(),
    }
    print('posts', posts)
    return render(request, 'store/dogs.html', data)


def show_post(request, post_slug):
    ''''Отображение раскрытого поста'''
    post = get_object_or_404(Store, slug=post_slug)
    print('Подпродукты')

    subProduct = list(post.sub_products.all())
    subProductList = list(Store.published.filter(title__in=subProduct))

    print(post.title)
    print(post.brand)
    print(post.cat2)
    print(post.size)

    products_by_flavor = {}
    productSlug = {}
    for product in subProductList:
        if product.taste not in products_by_flavor:
            products_by_flavor[product.taste] = [product]
            productSlug[product.taste] = [product.slug]
        else:
            products_by_flavor[product.taste].append(product)
            productSlug[product.taste].append(product.slug)

    print('products_by_flavor', products_by_flavor)
    print('productSlug', productSlug)

    data = {
        'post': post,
    }
    return render(request, 'store/post.html', data)


def info(request):
    return render(request, 'store/info.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
