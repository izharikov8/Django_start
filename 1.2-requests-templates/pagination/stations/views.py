import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def read_file():
    data = []
    with open('./data-398-2018-08-30.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return data


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = read_file()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    context = {
       'bus_stations': list(page),
       'page': page
    }
    return render(request, 'stations/index.html', context)




