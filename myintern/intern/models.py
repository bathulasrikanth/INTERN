from django.db import models




class User(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(max_length=50, blank=True, null=True)
    oauth_tokens = models.JSONField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    time_zone = models.CharField(max_length=50, blank=True, null=True)
    preferences = models.JSONField(blank=True, null=True)
    language = models.CharField(max_length=20, default="en")
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    last_password_change = models.DateTimeField(null=True, blank=True)



class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=50)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)
    priority = models.CharField(max_length=20, default="normal")


class Agency(models.Model):
    name = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=150)
    registration_number = models.CharField(max_length=50, unique=True)
    company_address = models.TextField()
    billing_address = models.TextField()
    website = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    primary_color = models.CharField(max_length=7, blank=True, null=True)  # Hex color code
    secondary_color = models.CharField(max_length=7, blank=True, null=True)
    billing_email = models.EmailField()
    support_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=50)
    currency = models.CharField(max_length=10, default="USD")
    language = models.CharField(max_length=20, default="en")
    subscription_status = models.CharField(max_length=20, default="active")
    subscription_plan = models.CharField(max_length=50, default="free")
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    settings = models.JSONField(blank=True, null=True)
    branding = models.JSONField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AgencySubscription(models.Model):
    agency = models.OneToOneField(Agency, on_delete=models.CASCADE, related_name='subscription')
    plan_name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=20, default="monthly")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default="active")
    team_member_limit = models.IntegerField(default=10)
    client_limit = models.IntegerField(default=10)
    features = models.JSONField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    last_payment_date = models.DateTimeField(null=True, blank=True)
    next_billing_date = models.DateTimeField(null=True, blank=True)



class AgencyBilling(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='billings')
    invoice_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="unpaid")
    due_date = models.DateTimeField()
    paid_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    line_items = models.JSONField(blank=True, null=True)
    currency = models.CharField(max_length=10, default="USD")
    is_paid = models.BooleanField(default=False)
    pdf_url = models.URLField(blank=True, null=True)


