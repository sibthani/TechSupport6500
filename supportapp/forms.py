from django import forms
from django.forms import ModelForm
from .models import *
from django.db import models  



class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ('issue_id',)


class CoachUserForm(forms.ModelForm):
    class Meta:
        model = CoachUser
        fields = '__all__'


class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = '__all__'


class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = '__all__'



class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'       


class Issue_CatgryForm(forms.ModelForm):
    class Meta:
        model = Issue_Catgry
        fields = '__all__'             