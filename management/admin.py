from django.contrib import admin

# Register your models here.
from .models import *

admin.sites.site.register(UserProfile)
admin.sites.site.register(District)
admin.sites.site.register(State)
admin.sites.site.register(Loan_Application)
admin.sites.site.register(Proofs)
admin.sites.site.register(KYC)
# admin.sites.site.register(Notes)

