from django.db import models
# need override django user default model
from django.contrib.auth.models import (PermissionsMixin,
                                        AbstractBaseUser,
                                        BaseUserManager)


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """create new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        # normal(ize email
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """create new superuser"""
        user = self.create_user(email,name,password)

        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """DataBase model for users in the system"""
    email = models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name user"""
        return self.name
    def get_short_name(self):
        """Retrive short naem user"""
        return self.name
    
    def __str__(self):
        return self.email





