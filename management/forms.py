from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from management.models import *

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted" or field!="is_verified":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"    
    class Meta:
        model = UserProfile
        fields = ("user", "role", "phone", "is_verified", "district")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
            
class LoanApplicationCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Loan_Application
        fields = ("full_name", "date_of_birth", "address", "landmark", "phone", "gender", "occupation", "organization", "email", "category", "loan_amount", "duration", "interest_rate", "emi_amount")


class ProofsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Proofs
        fields = ("bank_statement", "id_proof", "govt_id", "alt_data")
        
                  
class StatusUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Loan_Application
        fields = ("accepted",)


