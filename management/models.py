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
    credit_score = models.CharField(max_length=3, default=20)
    credit_limit = models.CharField(max_length=15, default=100000)
    is_verified = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
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
        ("Business Loan", "business_loan"),
        ("Medical Loan", "medical_loan"),
        ("Other", "other"),
    )
    ACCEPTED_CHOICES = (
        ("accepted", "accepted"),
        ("rejected", "rejected"),
        ("in_review", "in_review"),
    )
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    landmark = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    loan_amount = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    interest_rate = models.CharField(max_length=5)
    emi_amount = models.CharField(max_length=20)
    accepted = models.CharField(max_length=100, choices=ACCEPTED_CHOICES, default="in_review")
    deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"


class Proofs(models.Model):
    email = models.CharField(max_length=50)
    bank_statement = models.FileField(upload_to="documents/bank/%Y/%m/%d")
    id_proof = models.FileField(upload_to="documents/id/%Y/%m/%d")
    govt_id = models.FileField(upload_to="documents/govtid/%Y/%m/%d")
    alt_data = models.FileField(upload_to="documents/alt/%Y/%m/%d", default=None)


class KYC(models.Model):
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.FileField(upload_to="kyc/bank/%Y/%m/%d")
    id_proof = models.FileField(upload_to="kyc/id/%Y/%m/%d")
    bank_statement = models.FileField(upload_to="kyc/alt/%Y/%m/%d")
    
# class Notes(models.Model):
#     GENDER_CHOICES = (
#         ("male", "male"),
#         ("female", "female"),
#         ("other", "other"),
#     )
#     CATEGORY_CHOICES = (
#         ("Education Loan", "education_loan"),
#         ("Home Loan", "home_loan"),
#         ("Business Loan", "business_loan"),
#         ("Medical Loan", "medical_loan"),
#         ("Other", "other"),
#     )
#     category = models.ForeignKey(Loan_Application, on_delete=models.CASCADE, blank=True, null=True)
#     loan_amount = models.CharField(max_length=20)
#     duration = models.ForeignKey(Loan_Application, on_delete=models.CASCADE, blank=True, null=True)
#     interest_rate = models.ForeignKey(Loan_Application, on_delete=models.CASCADE, blank=True, null=True)
#     emi_amount = models.CharField(max_length=20)
#     accepted = models.BooleanField(default=False)
#     deleted = models.ForeignKey(Loan_Application, on_delete=models.CASCADE)
#     created_date = models.ForeignKey(Loan_Application, on_delete=models.CASCADE)
#     accepted_date = models.DateTimeField(auto_now=True)
#     last_repayment_date = models.DateTimeField(auto_now=True)
#     emi_number = models.CharField(max_length=20)
#     is_completed = models.BooleanField(default=False)

