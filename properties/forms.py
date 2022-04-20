from django import forms 
from django.forms import ModelForm
#from django.forms import ModelForms
from properties.models import Property




#   create the form used to upload property listings
#   use this form if uploading with an API
#   Put a  JQUERY click action on the button to send upload request to the API
class AddPropertyListingForm(forms.Form):
    
    PROPERTY_TYPE={
       ('BUNGALOW','BUNGALOW'),
       ('DETACHED','DETACHED'),
       ('SEMI-DETACHED','SEMI-DETACHED'),
       ('TERRACED','TERRACED'),
       ('APPARTMENT','APPARTMENT'),
       ('SITE','SITE'),
       ('PARKING SPACE','PARKING SPACE')
    }

   
    LISTING_TYPE={
       ('FOR SALE','FOR SALE'),
       ('FOR LEASE','FOR LEASE'),
    }
        
    
    BEDROOMS = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('9+','9+'),
    }
    
    
    COUNTIES = {
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Derry', 'Derry'),
        ('Donegal', 'Donegal'),
        ('Down', 'Down'),
        ('Dublin', 'Dublin'),
        ('Fermanagh', 'Fermanagh'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Tyrone', 'Tyrone'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    }
    
    BER_RATING = {
        ('A1','A1'),
        ('A2','A2'),
        ('A3','A3'),
        ('B1','B1'),
        ('B2','B2'),
        ('B3','B3'),
        ('C1','C1'),
        ('C2','C2'),
        ('C3','C3'),
        ('D1','D1'),
        ('D2','D2'),
        ('E1','E1'),
        ('E2','E2'),
        ('F','F'),
        ('G','G')
    }
    
    property_type = forms.CharField(
        label='Property Type',
        max_length = 20,
        widget = forms.Select(choices=PROPERTY_TYPE, attrs={'class':'form-control'})
    ) 
    
    
    listing_type = forms.CharField(
        label='Listing Type',
        max_length = 20,
        widget = forms.Select(choices=LISTING_TYPE, attrs={'class':'form-control'})
    ) 
    
    street_address = forms.CharField(
        label='Street Address',
        max_length = 64,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    county = forms.CharField(
        label='County',
        max_length = 12,
        widget = forms.Select(choices=COUNTIES, attrs={'class':'form-control'})
    )
    
    latitude = forms.CharField(
        label='Latitude',
        max_length = 30,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    
    longitude = forms.CharField(
        label='Longitude',
        max_length = 30,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    
    bedrooms = forms.CharField(
        label='Bedrooms',
        max_length = 5,
        widget = forms.Select(choices=BEDROOMS, attrs={'class':'form-control'})
    ) 
    
    ber_rating = forms.CharField(
        label='BER Rating',
        max_length = 20,
        widget = forms.Select(choices=BER_RATING, attrs={'class':'form-control'})
    ) 
    
    description = forms.CharField(
        label='Description',
        max_length = 600,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    price = forms.CharField(
        label='Price',
        max_length = 30,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    agent_email = forms.CharField(
        label='Agent Email',
        max_length = 64,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )


    #   Associate the class against the form
    #   Define which fiels should be displayed
    class Meta:
        model = Property
        #fields = ('property_type','listing_type','street_address','county','latitude','longitude','bedrooms','ber_rating','description','price',)
        
        
# create the form used to upload property listings
#   Use this form for uploading direct to DB
class AddPropertyListingForm2(ModelForm):
    class Meta:
        model = Property
        fields = ['property_type','listing_type','street_address','county','latitude','longitude','bedrooms','ber_rating','description','price', 'agent_email']
        
        
        '''
        PROPERTY_TYPE={
           ('BUNGALOW','BUNGALOW'),
           ('DETACHED','DETACHED'),
           ('SEMI-DETACHED','SEMI-DETACHED'),
           ('TERRACED','TERRACED'),
           ('APPARTMENT','APPARTMENT'),
           ('SITE','SITE'),
           ('PARKING SPACE','PARKING SPACE')
        }

   
        LISTING_TYPE={
           ('FOR SALE','FOR SALE'),
           ('FOR LEASE','FOR LEASE'),
        }
        
    
        BEDROOMS = {
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10+','10+'),
        }
        
    
        COUNTIES = {
            ('Antrim', 'Antrim'),
            ('Armagh', 'Armagh'),
            ('Carlow', 'Carlow'),
            ('Cavan', 'Cavan'),
            ('Clare', 'Clare'),
            ('Cork', 'Cork'),
            ('Derry', 'Derry'),
            ('Donegal', 'Donegal'),
            ('Down', 'Down'),
            ('Dublin', 'Dublin'),
            ('Fermanagh', 'Fermanagh'),
            ('Galway', 'Galway'),
            ('Kerry', 'Kerry'),
            ('Kildare', 'Kildare'),
            ('Kilkenny', 'Kilkenny'),
            ('Laois', 'Laois'),
            ('Leitrim', 'Leitrim'),
            ('Limerick', 'Limerick'),
            ('Longford', 'Longford'),
            ('Louth', 'Louth'),
            ('Mayo', 'Mayo'),
            ('Meath', 'Meath'),
            ('Monaghan', 'Monaghan'),
            ('Offaly', 'Offaly'),
            ('Roscommon', 'Roscommon'),
            ('Sligo', 'Sligo'),
            ('Tipperary', 'Tipperary'),
            ('Tyrone', 'Tyrone'),
            ('Waterford', 'Waterford'),
            ('Westmeath', 'Westmeath'),
            ('Wexford', 'Wexford'),
            ('Wicklow', 'Wicklow'),
        }
    
        BER_RATING = {
            ('A1','A1'),
            ('A2','A2'),
            ('A3','A3'),
            ('B1','B1'),
            ('B2','B2'),
            ('B3','B3'),
            ('C1','C1'),
            ('C2','C2'),
            ('C3','C3'),
            ('D1','D1'),
            ('D2','D2'),
            ('E1','E1'),
            ('E2','E2'),
            ('F','F'),
            ('G','G')
        }
    
        fields = ['street_address']
        street_address = forms.TextInput(attrs={'id': 'id_street_address', 'class':'form-control'})
        first_name = forms.TextInput(attrs={'id': 'firstname',  'class':'form-control'})
'''