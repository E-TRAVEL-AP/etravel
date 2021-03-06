from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.auth.models import User
import random
#For API
from amadeus import Client, ResponseError, Location
import json
from datetime import datetime
from django.http import HttpResponse
from iata_codes import IATACodesClient



locations = ["PUNE (PNQ)", "NEW DELHI (DEL)", "MUMBAI (BOM)", "LONDON (LON)", "BANGKOK (BKK)", "SYDNEY (SYD)", "NEW YORK CITY(NYC)", "PARIS (PAR)"]
codes = ["PNQ", "DEL", "BOM", "LON", "BKK", "SYD", "NYC", "PAR"]
#################################################
#API KEYS


amadeus = Client(client_id='t7HkaagNkZgxjG30TXfpjtmWQKRXO0U3', 
                 client_secret='w4PbnQiOa0XV3gQt')




#######################################################################################################################################

def homepage(request):
    location_name = locations
   

    return render(request, 'hotels/homepage.html',  {'location_name': location_name})

#######################################################################################################################################

#######################################################################################################################################

def hotels(request):



    origin = request.POST.get('Origin')
    departureDate = request.POST.get('Departuredate')
    returnDate = request.POST.get('Returndate')
    adults = request.POST.get('adults')
    children = request.POST.get('children')
    people= 0
    
    hotel_images = ["../../static/images/hotel1.jpg", "../../static/images/hotel2.jpg","../../static/images/hotel3.jpg","../../static/images/hotel4.jpg","../../static/images/hotel5.jpg","../../static/images/hotel6.jpg","../../static/images/hotel7.jpg","../../static/images/hotel8.jpg","../../static/images/hotel9.jpg", "../../static/images/hotel10.jpg", "../../static/images/hotel11.jpg", "../../static/images/hotel12.jpg", "../../static/images/hotel13.jpg", "../../static/images/hotel14.jpg", "../../static/images/hotel15.jpg", "../../static/images/hotel16.jpg"]



    kwargs = {'cityCode': origin,
              }
    
    location_name = locations
    #codes = ["PNQ", "DEL", "BOM", "LON", "BKK", "SYD"]
    hotelResult = []
    if origin and departureDate and returnDate:
        kwargs['cityCode'] = kwargs['cityCode'].upper()
        
        o = kwargs['cityCode']
        for i in range(len(location_name)):    
            if o == location_name[i]:
                 kwargs['cityCode'] = codes[i]
        try:
            response = amadeus.shopping.hotel_offers.get(**kwargs)
            hotelsjason = response.data

            

            
            for hotel in hotelsjason:

                price = hotel['offers'][0]['price']['total']
                name = hotel['hotel']['name']
                hotelID = hotel['hotel']['hotelId']
                distance = hotel['hotel']['hotelDistance']['distance']
                hotelImg = random.choice(hotel_images)

                Covid= bool(random.getrandbits(1))
                Parking= bool(random.getrandbits(1))
                Heritage= bool(random.getrandbits(1))
                Pool= bool(random.getrandbits(1))
                Gym= bool(random.getrandbits(1))
                HotBath= bool(random.getrandbits(1))
                 

                
                try:
                    descriptionFull = hotel['hotel']['description']['text']
                    descriptionFull = (descriptionFull[:1000] + '...') if len(descriptionFull) > 75 else descriptionFull
                    description = (descriptionFull[:125] + '...') if len(descriptionFull) > 75 else descriptionFull
                except:
                    description = "This is covid friendly Hotel with the amenities. Please visit!"
                    descriptionFull = description 
                address = hotel['hotel']['address']['lines']

                adults = int(adults)
                children = int(children)
                people = adults + children
                rooms = int(people/3 - 0.01) + 1
                totalPrice = rooms*(float(price))
                totalPrice = round(totalPrice, 2)
                searchedFlight = {'price': price, 'rooms': rooms, 'totalPrice': totalPrice, 'price': price, 'name':name, 'hotelID': hotelID, 'distance': distance, 'hotelImg': hotelImg, 'description': description, 'descriptionFull': descriptionFull,  'address': address, 'Covid':Covid, 'Parking':Parking, 'Heritage':Heritage, 'Pool':Pool, 'Gym':Gym, 'HotBath':HotBath}    
                hotelResult.append(searchedFlight)
            
            print(hotelResult)
            
            return render(request, 'hotels/hotels.html', {'hotelResult': hotelResult,
                                                         'origin': origin.upper(),
                                                         'departureDate': departureDate,
                                                         'returnDate': returnDate,
                                                         'people': people,
                                                         'location_name': location_name,})
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
            return render(request, 'hotels/hotels.html', {'location_name': location_name}) 
            
    


    return render(request, 'hotels/hotels.html', {'location_name': location_name}) 

#######################################################################################################################################

#######################################################################################################################################

def flights(request):
    
    

    origin = request.POST.get('Origin')
    destination = request.POST.get('Destination')
    departureDate = request.POST.get('Departuredate')
    returnDate = request.POST.get('Returndate')
    adults = (request.POST.get('adults'))
    children = (request.POST.get('children'))
    

    flightResults = []

    if not adults:
        adults = 1

    kwargs = {'originLocationCode': origin,
              'destinationLocationCode': destination,
              'departureDate': departureDate,
              'adults': adults
              }

    location_name = locations

    data = amadeus.reference_data.locations.get(keyword=request.GET.get('{origin}', None),
                                                    subType=Location.ANY).data
       
    print(data)

    if origin and destination and departureDate:
        
        kwargs['originLocationCode'] = kwargs['originLocationCode'].upper()
        kwargs['destinationLocationCode'] = kwargs['destinationLocationCode'].upper()
        
        o =  kwargs['originLocationCode']
        d = kwargs['destinationLocationCode']
        for i in range(len(location_name)):    
            if o == location_name[i]:
                kwargs['originLocationCode'] = codes[i]
            if d == location_name[i]:
                kwargs['destinationLocationCode'] = codes[i]
              

        try:
            response = amadeus.shopping.flight_offers_search.get(**kwargs)
            flightsjason = response.data

            
            for flight in flightsjason:

                price = flight['price']['total']

                
                flightID = flight['id']
                searchedFlight = []

                
                index = 0
                for itinaties in flight['itineraries']:

                    if len(flight['itineraries'][index]['segments']) == 2:

                        
                        
                        airlineCarrier = flight['itineraries'][index]['segments'][0]['carrierCode']
                        DepartureDate = get_hour(flight['itineraries'][index]['segments'][0]['departure']['at'])
                        firstFlightArrivalAirport = flight['itineraries'][index]['segments'][0]['arrival']['iataCode']
                        firstFlightArrivalDate = get_hour(flight['itineraries'][index]['segments'][0]['arrival']['at'])
                        firstFlightArrivalDuration = flight['itineraries'][index]['segments'][0]['duration']
                        secondFlightDepartureAirport = flight['itineraries'][index]['segments'][1]['departure']['iataCode']
                        secondFlightDepartureDate = get_hour(flight['itineraries'][index]['segments'][1]['departure']['at'])
                        
                        secondFlightAirline = flight['itineraries'][index]['segments'][1]['carrierCode']
                        secondFlightArrivalAirport = flight['itineraries'][index]['segments'][1]['arrival']['iataCode']
                        ArrivalDate = get_hour(flight['itineraries'][index]['segments'][1]['arrival']['at'])
                        secondFlightArrivalDuration = flight['itineraries'][index]['segments'][1]['duration']
                        Duration = flight['itineraries'][index]['duration'][2:]
                        availableseats = random.randint(1,100)

                        numberofStops = 1

                        
                        
                        
                    elif len(flight['itineraries'][index]['segments']) == 1:

                        
                        
                        airlineCarrier = flight['itineraries'][index]['segments'][0]['carrierCode']
                        DepartureDate = get_hour(flight['itineraries'][index]['segments'][0]['departure']['at'])
                        
                        
                        ArrivalDate = get_hour(flight['itineraries'][index]['segments'][0]['arrival']['at'])
                        firstFlightArrivalDuration = flight['itineraries'][index]['segments'][0]['duration']
                        Duration = flight['itineraries'][index]['duration'][2:]
                        availableseats = random.randint(1,100)

                        numberofStops = 0

                    index += 1
                adults = int(adults)
                children = int(children)
                price1 = float(price)
                totalPrice = adults*price1 + 0.67*children*price1  
                totalPrice = round(totalPrice, 2) 
                searchedFlight = {'airlineCarrier':airlineCarrier, 'DepartureTime': DepartureDate, 'Duration': Duration, 'ArrivalTime': ArrivalDate, 'numberofStops': numberofStops, 'price': price, 'totalPrice': totalPrice, 'flightID': flightID, 'availableseats':availableseats}    
                flightResults.append(searchedFlight)
        
            return render(request, 'hotels/flights.html', {'flightResults':flightResults,'origin': origin.upper(),
                                                     'destination': destination.upper(),
                                                     'departureDate': departureDate,
                                                     'returnDate': returnDate,
                                                     'adults': adults,
                                                     'children': children,
                                                     'location_name' : location_name,})
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error)
            return render(request, 'hotels/flights.html', {'location_name' : location_name}) 
            
    


    return render(request, 'hotels/flights.html', {'location_name' : location_name}) 

#######################################################################################################################################


#######################################################################################################################################



def get_hour(date_time):
    return datetime.strptime(date_time[0:19], "%Y-%m-%dT%H:%M:%S").strftime("%H:%M")

    

#######################################################################################################################################


#######################################################################################################################################


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Enter your first name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'email',)


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.data.get('first_name')
            email = form.cleaned_data.get('email')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)

            subject = 'Travel with Us!!'
            message = f'Hi {first_name},\nThank you for registering on JARThreeDeeWale!! \nEnjoy shopping on our site!'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email, ] 
            send_mail( subject, message, email_from, recipient_list ) 

            return redirect("/")

            

            
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            

    form = SignUpForm
    context = {'form': form}
    return render(request, "hotels/register.html", context)

#######################################################################################################################################

def logout_request(request):
    logout(request)
    return redirect("/")
    # messages.info(request, "logged out succesfully")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")


    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "hotels/login.html", context)

#######################################################################################################################################

def profile(request):
    
    if request.user.is_authenticated:

        userId = request.user.id
        Currentuser = User.objects.get(id=userId)
        email = Currentuser.email        
        user = request.user.get_username().capitalize() 
        name = request.user.get_full_name().capitalize()
        id = random.randint(2000,5000)
        
        return render(request, "hotels/profile.html", {'user':user, 'name':name, 'id':id, 'email':email})     
    

    return render(request, "hotels/profile.html", {})