from email.policy import default
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class MyUserManager(BaseUserManager):

    def create_superuser(self, username, email, password, **additional_fields):
        
        additional_fields.setdefault('is_staff', True)
        additional_fields.setdefault('is_superuser', True)
        additional_fields.setdefault('is_active', True)

        if additional_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if additional_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, email, password, **additional_fields)
    
    def create_user(self, username, email, password, **additional_fields):
        if not email:
            raise ValueError(_('Вы должны преоставить действительный email'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **additional_fields)
        user.set_password(password)
        user.save()
    
    

class MyUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Имя пользователя', max_length=100, unique=True)
    email = models.EmailField('Электронная почта', max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    start_date = models.DateTimeField('дата регистрации', default=timezone.now)
    about = models.TextField('Обо мне', max_length=700, blank=True)
    slug = models.SlugField(max_length=150, default='')

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username





