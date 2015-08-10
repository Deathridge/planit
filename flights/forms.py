from django import forms

class SubmitFlight(forms.Form):	
	FlightCode = forms.CharField(label='FlightCode', widget=forms.TextInput(attrs={'placeholder': 'Enter Flight code', 'class': 'form-control'}))
	DepartureDate = forms.DateField(label='Departs',widget=forms.DateInput(attrs={'placeholder': 'Enter Departure date', 'class': 'datepicker'}))
	
