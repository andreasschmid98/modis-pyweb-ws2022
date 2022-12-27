from django import forms
from django.forms import ModelForm
from .models import Module, User, Lecturer


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = '__all__'
        widgets = {
            'semesters': forms.CheckboxSelectMultiple,
            'graduate_programs': forms.CheckboxSelectMultiple,
            'specialisation_tracks': forms.CheckboxSelectMultiple,
        }
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
        user = kwargs.pop('user')
        super(ModuleForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'Dies ist ein Pflichtfeld.'}

        if user.user_type != user.ADMIN:
            self.fields.pop('lecturer')

    def save(self, user=None, commit=True):
        instance = super(ModuleForm, self).save(commit=False)

        if user is not None:
            if user.user_type != user.ADMIN:
                instance.lecturer = Lecturer.objects.get(user=user)
        if commit:
            instance.save()
        return instance
