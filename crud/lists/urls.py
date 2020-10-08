from django.urls import path
from . import views

urlpatterns = [
    path('list',views.countriesList,name="countries-list"),
    path('create',views.insertData,name="create-countries")
]