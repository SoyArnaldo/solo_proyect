from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
import os

class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, **kwargs):
		if not email:
			raise ValueError("El email es obligatorio")
		email = self.normalize_email(email)
		user = self.model(email = email, **kwargs)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)
		return self._create_user( email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")
		return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	def image_upload_to(self, instance = None):
		if instance:
			return os.path.join("User", self.username, instance)
		return None
	
	username = models.CharField(max_length= 50, unique= True, blank= False)
	first_name = models.CharField(max_length= 50, blank=True)
	last_name = models.CharField(max_length= 50, blank=True)
	email = models.EmailField(
		unique=True, blank = False,
		validators =
			[
				EmailValidator(message = "Por favor ingresa un email válido")
			]
	)
	password = models.CharField(max_length=128)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	image = models.ImageField(default="default/default-user.jpg", upload_to= image_upload_to)

	USERNAME_FIELD = "email"
	
	objects = CustomUserManager()
	
	def clean(self) -> None:
		super().clean()
		if CustomUser.objects.exclude(pk = self.pk).filter(email = self.email).exists():
			raise ValidationError("Este correo electrónico ya está en uso")
	
		if self.email.split("@")[1] != "gmail.com":
			raise ValidationError("Este correo electrónico no existe")
	
	def save(self, *args, **kwargs):
		self.full_clean()
		super().save( *args, **kwargs)

	def __str__(self) -> str:
		return f"{self.username} + {self.email}"

	class Meta():
		db_table = "users"