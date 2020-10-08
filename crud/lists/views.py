from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Country
import json
import os

# Create your views here.

def insertData(request):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'Countries.json')
    with open(my_file) as countries:
        country_json = json.load(countries)
    
    for country in country_json:
        data = Country(name=country['name'],
        full_name=country['full_name'],
        capital=country['capital'],
        currency=country['currency'],
        currency_code=country['currency_code'],
        citizenship=country['citizenship'])
        
        data.save()

    return Response('Data Inserted Successfully')

@api_view(['GET'])
def countriesList(request):
    tasks = Country.objects.all()
    serialize = CountrySerializer(tasks,many=True)

    response = {
        'success': True,
        'message':'Countries List',
        'list': serialize.data
    }
    return Response(response)
