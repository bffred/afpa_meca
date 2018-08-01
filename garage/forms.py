from django import forms

from django.forms import ModelForm, TextInput, EmailInput, SelectDateWidget, FileInput, NumberInput, DateInput
from django.forms.utils import ErrorList
from .models import Client, DonneesPersonnelles, Address, ZipCode, City, Motorise, Voiture

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ["nom_client", "prenom_client", "numero_afpa_client"]
        widgets = {
            'nom_client': TextInput(attrs={'class': 'form-control'}),
            'prenom_client': TextInput(attrs={'class': 'form-control'}),
            'numero_afpa_client': NumberInput(attrs={'class': 'form-control'})
        }


class DonneesPersonnellesForm(forms.ModelForm):
    class Meta:
        model = DonneesPersonnelles
        fields = ["mail_client", "telephone_client","carte_AFPA_img"]
        widgets = {
            'mail_client': TextInput(attrs={'class': 'form-control'}),
            'telephone_client': TextInput(attrs={'class': 'form-control'}),
            'carte_AFPA_img': FileInput(attrs={'class': 'form-control'})
        }  


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["street","street_number","street_complement"]
        widgets = {
            'street': TextInput(attrs={'class': 'form-control'}),
            'street_number': NumberInput(attrs={'class': 'form-control'}),
            'street_complement': TextInput(attrs={'class': 'form-control'})
        }



class ZipCodeForm(forms.ModelForm):
    class Meta:
        model = ZipCode
        fields = ["zip_code"]
        widgets = {
            'zip_code': TextInput(attrs={'class': 'form-control'})
        }  


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city_name"]
        widgets = {
            'city_name': TextInput(attrs={'class': 'form-control'})
        }  

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = '__all__'
        widgets = {
            'libelle_marque': TextInput(attrs={'class': 'form-control'}),
            'libelle_modele': TextInput(attrs={'class': 'form-control'}),
            'immatriculation': TextInput(attrs={'class': 'form-control'}),
            'vin': TextInput(attrs={'class': 'form-control'}),
            'kilometrage': NumberInput(attrs={'class': 'form-control'}),
            'date_mec': DateInput(attrs={'class': 'form-control'}),
            'carte_grise_img': FileInput(attrs={'class': 'form-control'}),
            'carte_assurance_img': FileInput(attrs={'class': 'form-control'})
        }
       
