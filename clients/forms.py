from django import forms 
from django.forms import ModelForm
from .models import ShiftingRequest, ChangePackage

#creating a shifting request form
class ShiftingRequestForm(ModelForm):
	class Meta:
		model = ShiftingRequest
		fields = ("name", "account","email","phonenumber","caretaker","streetname","bname","landmark")

class ChangePackageForm(ModelForm):
	class Meta:
		model = ChangePackage
		fields = ("account","email","package_type")

class CheckoutForm(ModelForm):
	class Meta:
		fields = ("address","client_number","zipcode","landmark2")