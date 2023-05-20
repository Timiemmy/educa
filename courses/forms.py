from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      # The fields that will be included in each form of the formset.
                                      fields=['title',
                                              'description'],
                                      # Allows you to set the number of empty extra forms to display in the formset.
                                      extra=2,
                                      can_delete=True)  # If you set this to True, Django will include a Boolean field for each form that will be rendered as a checkbox input. It allows you to mark the objects that you want to delete.
