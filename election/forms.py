from django import forms

class VoteForm(forms.Form):
	CHOICES=[('','select 1'),
	         ('select2','select 2')]

	chairperson = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    