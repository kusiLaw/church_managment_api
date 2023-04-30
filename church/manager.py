from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
  '''
    Custom user manage to check email since it will be used
    for authentication instead of username
  '''

  def create_user(self, email, password, **extra_fields):
    """
        Create and save a user with the given email and password.
    """
    print(
       email,"  Email \n",
       password, " password",
       extra_fields
    )
    if not email:
      raise ValueError("Email equired")
    if not password:
      raise ValueError("Password required")
    user = self.model(self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, password,**extra_fields ):
    """
    Create and save a SuperUser with the given email and password.
    """
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_active", True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError(_("Superuser must have is_staff=True."))
    if extra_fields.get("is_superuser") is not True:
        raise ValueError(_("Superuser must have is_superuser=True."))
    return self.create_user(email, password, **extra_fields)