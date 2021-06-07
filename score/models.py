from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid as uuid_lib

# Create your models here.
# Post → Userと読み替える
class Record(models.Model):
    wins = models.IntegerField(null=False, default=0)
    loses = models.IntegerField(null=False, default=0)
    ties = models.IntegerField(null=False, default=0)


class User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	records = models.OneToOneField(Record, on_delete=models.CASCADE)

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
	



