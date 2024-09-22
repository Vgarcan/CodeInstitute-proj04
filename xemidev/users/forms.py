from allauth.account.forms import SignupForm
from django import forms


class SignupForm(SignupForm):
    """
    Custom form for user registration. Includes additional fields for storing user contact details.
    """
    # phone_number = forms.CharField(max_length=20)
    # company_name = forms.CharField(max_length=100)
    # company_address = forms.CharField(max_length=250)
    # company_type = forms.CharField(max_length=100)

    def save(self, request):
        user = super().save(request)
        # user.phone_number = self.cleaned_data['phone_number']
        # user.company_name = self.cleaned_data['company_name']
        # user.company_address = self.cleaned_data['company_address']
        # user.company_type = self.cleaned_data['company_type']
        user.save()
        return user
