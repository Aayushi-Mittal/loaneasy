from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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
        return Loan_Application.objects.filter(deleted=False)
    

class LenderLoanApplicationsListView(ListView):
    queryset = Notes.objects.filter(deleted=False)
    template_name = "dashboard.html"
    context_object_name = "loan_notes"
    paginate_by = 10

    def get_queryset(self):
        return Notes.objects.filter(deleted=False)


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


class LoanApplicationDeleteView(DeleteView):
    model = Loan_Application
    template_name = "delete.html"
    success_url = "/dashboard/"


class LoanApplicationDetailView(DetailView):
    model = Loan_Application
    template_name = "loan_application_details.html"


class LoanApplicationStatusUpdateView(UpdateView):
    model = Loan_Application
    form_class = StatusUpdateForm
    template_name = "update_status.html"
    success_url = "/dashboard/"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
