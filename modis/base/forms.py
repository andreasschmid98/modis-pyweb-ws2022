from django import forms
from django.forms import ModelForm

from .models import Module, Lecturer


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

        # Custom widgets for the form
        widgets = {
            'semesters': forms.CheckboxSelectMultiple,
            'graduate_programs': forms.CheckboxSelectMultiple,
            'specialisation_tracks': forms.CheckboxSelectMultiple,
        }

        # Custom labels for the form
        labels = {
            'title': 'Titel',
            'content': 'Inhalt',
            'learning_objective': 'Lernziele',
            'lecturer': 'Verantwortlicher',
            'semesters': 'Semester',
            'graduate_programs': 'Studiengänge',
            'specialisation_tracks': 'Vertiefungsanrechnung',
            'credits': 'Credits'
        }

    def __init__(self, *args, **kwargs):
        # Get the current user
        user = kwargs.pop('user')
        super(ModuleForm, self).__init__(*args, **kwargs)

        # Delete the lecturer field from the form (only ADMIN is allowed to set the lecturer manually)
        if user.user_type != user.ADMIN:
            self.fields.pop('lecturer')

        # Initialize custom error messages for required fields
        for field in self.fields.values():
            field.error_messages = {'required': 'Dies ist ein Pflichtfeld.'}

    def save(self, user=None, commit=True):
        instance = super(ModuleForm, self).save(commit=False)

        # Set the logged-in lecturer as the lecturer of the module
        if user is not None:
            if user.user_type != user.ADMIN:
                instance.lecturer = Lecturer.objects.get(user=user)
        if commit:
            instance.save()
        return instance
