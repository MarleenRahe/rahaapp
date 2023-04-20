from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your forms here.

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class NewDeptForm(forms.Form):
    name = forms.CharField(label="Võlausaldaja")
    amount = forms.IntegerField(label="Võlgu oldav summa", validators=[MinValueValidator(0)])
