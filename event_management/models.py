from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from event_management.views import UserManager
# Create your models here.


class User(AbstractUser):
    # add additional fields in here
    age=models.CharField(max_length=3)
    address=models.TextField()
    phone_number=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.username

class Event(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    event_image = models.FileField(blank=True, upload_to="media")
    payment_status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return self.name

# class User(AbstractBaseUser):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name