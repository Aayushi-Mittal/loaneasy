from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('dashboard/', LoanApplicationsListView.as_view()),
    # path('dashboard/', BorrowerLoanApplicationsListView.as_view()),
    # path('admin/dashboard/', AdminLoanApplicationsListView.as_view()),
    # path('lender/dashboard/', LenderLoanApplicationsListView.as_view()),
    path('loan-application/', LoanApplicationCreateView.as_view()),
    path('proofs/', ProofsCreateView.as_view()),
    path('kyc/', UserLoginView.as_view()),
]
