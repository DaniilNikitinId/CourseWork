from django.urls import path, re_path, register_converter
from . import views

# from . import converters


# register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/', views.cats, name='cats'),
    path('cats/CatsSterilized', views.CatsSterilized, name='CatsSterilized'),
    path('cats/kittens', views.kittens, name='kittens'),
    path('cats/dietsCats', views.dietsCats, name='dietsCats'),

    path('dogs/', views.dogs, name='dogs'),
    path('dogs/bigDogs', views.bigDogs, name='bigDogs'),
    path('dogs/mediumDogs', views.mediumDogs, name='mediumDogs'),
    path('dogs/smallDogs', views.smallDogs, name='smallDogs'),
    path('dogs/dietsDogs', views.dietsDogs, name='dietsDogs'),
    path('dogs/puppies', views.puppies, name='puppies'),

    path('searchCats/', views.searchCats, name='searchCats'),
    path('searchDogs/', views.searchDogs, name='searchDogs'),

    path('filterCats/', views.filterCats, name='filterCats'),
    path('filterDogs/', views.filterDogs, name='filterDogs'),

    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('info/', views.info, name='info'),


]
