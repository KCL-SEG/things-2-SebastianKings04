"""Forms of the project."""
from things import models
from django import forms

class ThingForm(forms.ModelForm):

    class Meta:

        model = models.Thing
        fields = ["name", "description" , "quantity"]
        widgets = {
            "description" : forms.Textarea,
            "quantity" : forms.NumberInput
        }
