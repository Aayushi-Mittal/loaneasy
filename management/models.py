import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class State(TimeStampMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class District(TimeStampMixin):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class UserProfile(TimeStampMixin):

    ROLE_CHOICES = (
        ("lender", "lender"),
        ("borrower", "borrower"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, blank=True, null=True
    )
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username}"


class Loan_Application(TimeStampMixin):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )
    CATEGORY_CHOICES = (
        ("Education Loan", "education_loan"),
        ("Home Loan", "home_loan"),
        ("Travel Loan", "travel_loan"),
        ("Medical Loan", "medical_loan"),
        ("Other", "other"),
    )
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    landmark = models.TextField()
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    emergency_phone_number = models.CharField(max_length=30)
    expired_time = models.DateTimeField(blank=True, null=True)
    occupation = models.CharField(max_length=30)
    organiization = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    loan_amount = models.CharField(max_length=20)
    duration = models.CharField(max_length=30)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"


class Proofs(models.Model):
    bank_statement = models.FileField(upload_to="documents/bank/%Y/%m/%d")
    id_proof = models.FileField(upload_to="documents/id/%Y/%m/%d")
    govt_id = models.FileField(upload_to="documents/govtid/%Y/%m/%d")
    bank_statement = models.FileField(upload_to="documents/alt/%Y/%m/%d")


class KYC(models.Model):
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.FileField(upload_to="kyc/bank/%Y/%m/%d")
    id_proof = models.FileField(upload_to="kyc/id/%Y/%m/%d")
    bank_statement = models.FileField(upload_to="kyc/alt/%Y/%m/%d")
