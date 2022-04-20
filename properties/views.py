from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
import requests
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from .models import Property, Receipt
from .forms import AddPropertyListingForm, AddPropertyListingForm2

#import sys
#import os
#import importlib

#from myclasses import LocalDB

#sys.path.append(os.path.realpath('modules'))
#local_db_module = importlib.import_module('LocalDB')

# Create your views here.



#def index(request):
 #   args = {}
   # return redirect('/properties/listing/')

def create_receipt(request, propertyId):
    
    print('create_receipt propertyId=' + propertyId)
    
    if request.method == 'POST':

        property = get_object_or_404(Property, pk=propertyId)

        receipt = Receipt()
        receipt.name = request.POST['name']
        receipt.date_receipt = request.POST['date_receipt']
        receipt.merchant_name = request.POST['merchant_name']
        receipt.amount_total = request.POST['amount_total']
        receipt.user = propertyId
        receipt.user_email = property.agent_email
        
        #print(json.dumps(model_to_dict(receipt)))
        
        url = settings.RECEIPT_API_URL + '/receipts/'
        headers = {'Authorization': settings.RECEIPT_API_TOKEN, 'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(model_to_dict(receipt)), headers=headers)
        messages.success(request, ("Receipt Addition Successful!"))

    context = {
        'propertyId': propertyId,
    }
    return render(request, 'receipt_create.html', context)

def update_receipt(request, receiptId, propertyId):

    print('update_receipt propertyId=' + propertyId + ', receiptId=' + receiptId)
    
    if request.method == 'POST':

        receipt = Receipt()
        receipt.id = receiptId
        receipt.name = request.POST['name']
        receipt.date_receipt = request.POST['date_receipt']
        receipt.merchant_name = request.POST['merchant_name']
        receipt.amount_total = request.POST['amount_total']
        receipt.user = request.POST['user']
        receipt.user_email = request.POST['user_email']

        url = settings.RECEIPT_API_URL + '/receipts/' + receiptId + '/'
        headers = {'Authorization': settings.RECEIPT_API_TOKEN, 'Content-Type': 'application/json'}
        response = requests.put(url, data=json.dumps(model_to_dict(receipt)), headers=headers)
        #print(response)
        messages.success(request, ("Receipt Update Successful!"))

    else:

        url = settings.RECEIPT_API_URL + '/receipts/' + receiptId + '/?format=json'
        headers = {'Authorization': settings.RECEIPT_API_TOKEN}
        response = requests.get(url, headers=headers)
        #convert reponse data into json
        receipt = response.json()

    context = {
        'receipt': receipt,
        'propertyId': propertyId,
    }
    return render(request, 'receipt_update.html', context)

def delete_receipt(request, receiptId, propertyId):

    print('delete_receipt propertyId=' + propertyId + ', receiptId=' + receiptId)

    isSubmitted = False
    if request.method == 'POST':

        receipt = Receipt()
        url = settings.RECEIPT_API_URL + '/receipts/' + receiptId + '/'
        headers = {'Authorization': settings.RECEIPT_API_TOKEN}
        response = requests.delete(url, headers=headers)
        messages.success(request, ("Receipt Deletion Successful!"))
        isSubmitted = True
    
    else:

        url = settings.RECEIPT_API_URL + '/receipts/' + receiptId + '/?format=json'
        headers = {'Authorization': settings.RECEIPT_API_TOKEN}
        response = requests.get(url, headers=headers)
        #convert reponse data into json
        receipt = response.json()

    context = {
        'receipt': receipt,
        'propertyId': propertyId,
        'isSubmitted' : isSubmitted,
    }
    return render(request, 'receipt_delete.html', context)

def listings(request, *args, **kwargs):
    
    print("in index view")
    print(args,kwargs)
    
    '''
    
    property_list = [
        {'id':'1','price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Cork'},
        {'id':'2','price':'€195,000','bedrooms':'2', 'address':'BLOSSOM & BERRY, Main Street, Lismore','county': 'Waterford'},
        {'id':'3','price':'€285,000','bedrooms':'4', 'address':'Kilmore, Dring','county': 'Longford'},
        {'id':'4','price':'€340,000','bedrooms':'4', 'address':'22 Mervue Crescent, Ballyvolane','county': 'Cork'},
        {'id':'5','price':'€495,000','bedrooms':'4', 'address':'The Rectory, Banse Glebe, Kilmanagh','county': 'Kilkenny'},
        {'id':'6','price':'€248,500','bedrooms':'4', 'address':'12 St MaryS Road, Kingscourt','county': 'Cavan'},
        {'id':'7','price':'€365,000','bedrooms':'3', 'address': '60 Mill View, Ballinglanna, Glanmire','county': 'Cork'},
        {'id':'8','price':'€295,000','bedrooms':'3', 'address':'3 The Alders, Cstlejane Woods, Glasmire','county': 'Cork'},
        {'id':'9','price':'€425,000','bedrooms':'4', 'address':'29 Stonebridge, Kells, Meath','county': 'Meath'},
        {'id':'10','price':'€485,000','bedrooms':'4', 'address':'Coolmona, Donoughmore','county': 'Cork'},
        {'id':'11','price':'€295,000','bedrooms':'4', 'address':'Roayal Oak Road, Bagenalstown','county': 'Carlow'},
        {'id':'12','price':'€400,000','bedrooms':'4', 'address':'75 The Wavering, Blainroe','county': 'Wicklow'},
        {'id':'13','price':'€410,000','bedrooms':'3', 'address':'106 Carlton Court, Swords','county': 'Dublin'},
        {'id':'14','price':'€240,000','bedrooms':'3', 'address':'12 Chestnut Grove, Casstlepark, Mallow','county': 'Cork'},
        {'id':'15','price':'€345,000','bedrooms':'5', 'address':'13 Woodlands, Abbeycartron','county': 'Longford'},
        {'id':'16','price':'€250,000','bedrooms':'4', 'address':'16 Francis Street, Rathealy, Fermoy','county': 'Cork'},
        {'id':'17','price':'€265,000','bedrooms':'4', 'address':'21 West Avenue, Lios Rua, Ballyvolane','county': 'Kerry'},
        {'id':'18','price':'€105,000','bedrooms':'2', 'address':'Main Street, Lismore','county': 'Wicklow'},
        {'id':'19','price':'€205,000','bedrooms':'4', 'address':'Lismore, Bring','county': 'Leitrim'},
        {'id':'20','price':'€300,000','bedrooms':'4', 'address':'103 Mervue, Ballyvolane','county': 'Limerick'},
        {'id':'21','price':'€405,000','bedrooms':'4', 'address':'Banse Glebe, Kilmanagh','county': 'Carlow'},
        {'id':'22','price':'€348,500','bedrooms':'4', 'address':'39 St MaryS Road, Kingscourt','county': 'Meath'},
        {'id':'23','price':'€260,000','bedrooms':'3', 'address': '12 Mill View, Ballinglanna, Glanmire','county': 'WestMeath'},
        {'id':'24','price':'€240,000','bedrooms':'3', 'address':'17 The Alders, Cstlejane Woods, Glasmire','county': 'Roscommon'},
        {'id':'25','price':'€600,000','bedrooms':'4', 'address':'35 Stonebridge, Kells, Meath','county': 'Donegal'},
        {'id':'26','price':'€415,000','bedrooms':'4', 'address':'Donoughmore','county': 'Sligo'},
        {'id':'27','price':'€245,000','bedrooms':'4', 'address':'Bagenalstown','county': 'Galway'},
        {'id':'28','price':'€300,000','bedrooms':'4', 'address':'51 The Wavering, Blainroe','county': 'Galway'},
        {'id':'29','price':'€320,000','bedrooms':'3', 'address':'19 Carlton Court, Swords','county': 'Laois'},
        {'id':'30','price':'€290,000','bedrooms':'3', 'address':'33 Chestnut Grove, Casstlepark, Mallow','county': 'Laois'},
        {'id':'31','price':'€275,000','bedrooms':'5', 'address':'40 Woodlands, Abbeycartron','county': 'Tipperary'},
        {'id':'32','price':'€270,000','bedrooms':'4', 'address':'4 Francis Street, Rathealy, Fermoy','county': 'Cork'},
    ]
    
    '''
    #   instantiate object for interacting with the database
    local_db = LocalDB()
    property_list_db = local_db.get_property_list()
    
    #Property.objects.all()
    
    p = Paginator(property_list_db,6)
    
    page = request.GET.get('page')
    property_page = p.get_page(page)

    args = {
        'heading':'Property Listing' ,
        'property_list': property_list_db,
        'property_page': property_page
    }
    
    #   cleanup: destroy the DB object
    del local_db
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'property_list.html',args)
    
    
#   display the detail of individual entertainers
def display_property_profile(request, property_id):
    
    print("in display_property_profile view")
    
    property = get_object_or_404(Property, pk=property_id)
    
    url = settings.RECEIPT_API_URL + '/receipts/?format=json'
    headers = {'Authorization': settings.RECEIPT_API_TOKEN}
    response = requests.get(url, headers=headers)
    #convert reponse data into json
    receipts = response.json()
    print(receipts)
    
    args = {'property': property, 'receipts': receipts}
    return render(request,'property_profile.html',args)
   

#   Upload details of a new Property 
def add_property_listing(request):
    table_name="properties"
    
    '''
        TO DO
        Add in the action for the form submission
        
        See timekeepr app companies views.py
    '''
    #   CHECK IF THE FORM WAS SUBMITTED
    #   If so, then read in the contents of the form
    if request.method == 'POST':
        form = AddPropertyListingForm2(request.POST)
        uploaded = False

                #   Check if the form contents is valid
        if form.is_valid():
            
            form.cleaned_data
            
            property_type = request.POST['property_type']
            listing_type = request.POST['listing_type']
            street_address = request.POST['street_address']
            county = request.POST['county']
            bedrooms = request.POST['bedrooms']
            ber_rating = request.POST['ber_rating']
            description = request.POST['description']
            price = request.POST['price']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            agent_email = request.POST['agent_email']
            
            property = {
                'property_type': property_type,
                'listing_type': listing_type,
                'street_address': street_address,
                'county': county,
                'bedrooms': bedrooms,
                'ber_rating': ber_rating,
                'description': description,
                'price': price,
                'latitude': latitude,
                'longitude': longitude,
                'agent_email': agent_email,
            }

        # NOW do a call to the localDB class to save the contents of the form
        #local_db = LocalDB()
        #uploaded = local_db.add_property(request,form)
        
        try:
            uploaded = form.save() # commit=False by default
            #text = form.clean('post')
        except Exception as e:
            print('form save failed')
            print(e)
        print('upoaded is ')
        print(uploaded)
        #   CHECK if the UPLOAD WAS SUCCESSFUL
        #   If yes, diplay the list 
        #   If no, display error
        if uploaded:
            return redirect(reverse('properties:listings'))
        else:
            return redirect(reverse('properties:property_add_error'))
    else:
        #   If the page was just browsed to
        #   Then load an empty form for uploading a property listing
        form = AddPropertyListingForm2()
        
        args = {'heading' : 'Add Property Listing', 'form': form}
        return render(request,'add_property_listing.html',args)
        

        
#   View to handle errors in uploading properties
def property_add_error(request):
    args = {'heading' : 'Upload Error'}
    print('property add error')
    return render(request,'property_add_error.html',args)  
    #return render(request,'add_property_listing.html',args)
    
##################################################################################
#    CLASS USED FOR INTERACTING WITH THE (LOCAL) DATABASE
##################################################################################

class LocalDB():
    
    #   INITIALISE
    def __init__(self):
        print('initialised')
        
    #   DESTROY THE OBJECT
    def __del__(self):
        print('DB Object Destroyed')
    
    #def add_a_property(self,table_name,property):
        
    def get_property_list(self):
        print('retrieving property list')
        return Property.objects.all().order_by('-id')
        
    def add_property(self, request,form):
        uploaded = False
        
        #   Check if the form contents is valid
        if form.is_valid():
            property_type = request.POST['property_type']
            listing_type = request.POST['listing_type']
            street_address = request.POST['street_address']
            county = request.POST['county']
            bedrooms = request.POST['bedrooms']
            ber_rating = request.POST['ber_rating']
            description = request.POST['description']
            price = request.POST['price']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            agent_email = request.POST['agent_email']
            
            property = {
                'property_type': property_type,
                'listing_type': listing_type,
                'street_address': street_address,
                'county': county,
                'bedrooms': bedrooms,
                'ber_rating': ber_rating,
                'description': description,
                'price': price,
                'latitude': latitude,
                'longitude': longitude,
                'agent_email': agent_email,
            }
            
            print('form submitted')
            print(property)
        
            try:
                uploaded = form.save()
                text = form.clean('post')
            except Exception as e:
                print('form save failed')
                print(e)

        return uploaded
