from django import forms
from django.forms import TextInput

from .models import Core
from .models import Project, Facility


class PostForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    required_css_class = 'required'
    Type_of_vehicle = forms.ChoiceField(choices=(('Bus', 'Bus'), ('Train', 'Train'), ('Car', 'Car')), widget=forms.RadioSelect(), required=False)
    Type_of_vehicle.widget.attrs.update({'class': 'form-control'})
    services = forms.ModelMultipleChoiceField(queryset=Facility.objects,  widget=forms.CheckboxSelectMultiple(), required=False)
    services.widget.attrs.update({'class': 'form-control'})
    Date_Of_Journey = forms.DateField(input_formats=['%d/%m/%Y'], widget=TextInput(attrs={'placeholder': 'Journey Date', 'autocomplete': 'off', 'class': 'form-control'}))
    Date_of_return = forms.DateField(input_formats=['%d/%m/%Y'], widget=TextInput(attrs={'placeholder': 'Return Date', 'autocomplete': 'off', 'class': 'form-control'}))
    Gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))

    class Meta:
        model = Project
        fields = ['Name',
                  'Age',
                  'Gender',
                  'Leaving_From',
                  'Going_To',
                  'Date_Of_Journey',
                  'Date_of_return',
                  'Additional_feature',
                  'services',
                  'Type_of_vehicle'
                  ]
