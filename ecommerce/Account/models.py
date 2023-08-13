from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from backend_apps.product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name,mobile_number, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            mobile_number=mobile_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name,mobile_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,  
            mobile_number=mobile_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




# created custome user  
class User (AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True),
    updated_at=models.DateTimeField(auto_now=True) 

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","mobile_number"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    




class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()  # Change the field name to 'comment'
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"