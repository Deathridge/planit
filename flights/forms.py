from django import forms

class SubmitFlight(forms.Form):	
	FlightCode = forms.CharField(label='FlightCode', widget=forms.TextInput(attrs={'placeholder': 'QF762', 'class': 'form-control'}))
	DepartureDate = forms.DateField(label='Departs',widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY', 'class': 'form-control datepicker'}))
	
