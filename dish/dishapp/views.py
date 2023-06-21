from django.shortcuts import render,redirect
import csv

from .models import Hotel_model


def home(request):
	print(request.headers)
	return render(request,"dishapp/home.html",{})

def welcome(request):
	print(request.headers)
	return render(request,"dishapp/welcome.html",{})


def import_csv(request):
    file_path = "static/restaurants_small.csv"
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            hotel = Hotel_model(
                name=row[1],
                location=row[2],
                items=row[3],
                lat_long=row[4],
                full_details=row[5]
            )
            hotel.save()

    return render(request, "dishapp/home.html")


def search_hotels(request):
    dish = request.GET.get('dish')

    if dish:
        hotels = Hotel_model.objects.filter(items__icontains=dish)
    else:
        hotels = []

    return render(request, 'dishapp/home.html', {'dish': dish, 'hotels': hotels})