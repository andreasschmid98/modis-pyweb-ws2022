from django.forms import ModelForm
from .models import Module, User, Lecturer


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        If a user is given to the function, we call the function via create_module. In order to raise no error,
        we have to pass {} for **kwargs instead of **kwargs
        """
        if 'user' in kwargs:
            super(ModuleForm, self).__init__(*args, {})
            if kwargs.get('user').user_type != User.ADMIN:
                self.fields.pop('lecturer')
        else:
            super(ModuleForm, self).__init__(*args, **kwargs)

    def save(self, user=None, commit=True):
        instance = super(ModuleForm, self).save(commit=False)
        if user is not None:
            if user.user_type != user.ADMIN:
                instance.lecturer = Lecturer.objects.get(user=user)
        if commit:
            instance.save()
        return instance
