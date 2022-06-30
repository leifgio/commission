from django.forms import ModelForm
from .models import Service, ArtistInformation
from django import forms

class CreateService(ModelForm):
    class Meta:
        model = Service
        fields = ['service_artist', 'service_client', 'service_date', 'service_type']

class CreateArtist(ModelForm):
    class Meta:
        model = ArtistInformation
        fields = ['artistname']
