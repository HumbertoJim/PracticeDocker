from django import forms

class FibonacciForm(forms.Form):
    steps = forms.IntegerField(
        initial=5,
        min_value=1,
        required=True,
        label='Steps',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-5'})
    )