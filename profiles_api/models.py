from django.db import models
# For customising default Django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for User Profile: Manipulates objects within the project"""

    def create_user(self, email, name, password = None):
        """Creates a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        
        user.set_password(password) # password is encrypted by hashing
        user.save(using = self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Creates a new superuser profile"""
        user = self.create_user(email, name, password)

        user.is_superuser = True #inherited from PermissionMixin
        user.is_staff = True
        user.save(using = self._db)

        return  user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the application
    """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() #yet to be made

    USERNAME_FIELD = 'email' #using email id as username for a profile
    REQUIRED_FIELDS = ['name'] #alongwith username what else is a required field

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.name
    
    def get_short_name(self):
        """Return short name of user"""
        return self.name
    
    #Recommended
    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE # if profile is removed, then profile feeds will be deleted
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
