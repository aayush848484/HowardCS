from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True, on_delete= models.CASCADE)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    classification_choices=(
        ('Freshman', 'Fr'),
        ('Sophomore', 'Sp'),
        ('Junior', 'Jr'),
        ('Senior', 'Sr')
    )
    classification = models.CharField(choices=classification_choices, max_length=10, default='Fr')

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)

    def get_classification(self):
        return self.user.profile.classification

    def get_full_name(self):
        return self.user.name

