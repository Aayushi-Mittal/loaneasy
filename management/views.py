from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from management.forms import *
from management.models import *


class UserCreateView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = "auth/create.html"
    success_url = "/login/"


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "login.html"
    success_url = "/dashboard/"
    
# class Dashboard(LoginRequiredMixin, TemplateView):
#     template_name = "auth/dashboard.html"


class LoanApplicationsListView(ListView):
    queryset = Loan_Application.objects.filter(deleted=False)
    template_name = "dashboard.html"
    context_object_name = "loan_application"
    paginate_by = 10

    def get_queryset(self):
        # accepted = Loan_Application.objects.filter(accepted='accepted', deleted=False)
        # in_review = Loan_Application.objects.filter(accepted='in_review', deleted=False)
        # rejected = Loan_Application.objects.filter(accepted='rejected', deleted=False)
        # output=[]
        # if accepted!=[]:
        #     output.append(accepted)
        # if in_review!=[]:
        #     output.append(in_review)
        # if rejected!=[]:
        #     output.append(rejected)
        # return output
        return Loan_Application.objects.filter(deleted=False)


# class BorrowerLoanApplicationsListView(ListView):
#     queryset = Loan_Application.objects.filter(deleted=False)
#     template_name = "borrower_dashboard.html"
#     context_object_name = "loan_application"
#     paginate_by = 10

#     def get_queryset(self):
#         return Loan_Application.objects.filter(deleted=False)

# class LenderLoanApplicationsListView(ListView):
#     queryset = Loan_Application.objects.filter(deleted=False)
#     template_name = "lender_dashboard.html"
#     context_object_name = "notes"
#     paginate_by = 10

#     def get_queryset(self):
#         return Loan_Application.filter(accepted=('accepted'), deleted=False)

# class AdminLoanApplicationsListView(ListView):
#     queryset = Loan_Application.objects.filter(deleted=False)
#     template_name = "admin_dashboard.html"
#     context_object_name = "loan_application"
#     paginate_by = 10

#     def get_queryset(self):
#         return Loan_Application.objects.filter(deleted=False)


class LoanApplicationCreateView(CreateView):
    model = Loan_Application
    form_class = LoanApplicationCreationForm
    template_name = "loan_application_1.html"
    success_url = "/dashboard/"



# def upload_file(request):
#     if request.method == 'POST':
#         form = ProofsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/proofs/')
#     else:
#         form = ProofsForm()
#     return render(request, 'loan_application_2.html', {'form': form})

class ProofsCreateView(CreateView):
    model = Proofs
    form_class = ProofsForm
    template_name = "loan_application_2.html"
    success_url = "/dashboard/"
    # upload_file(request)
