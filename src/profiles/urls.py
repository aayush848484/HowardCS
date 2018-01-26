from django.conf.urls import url
from . import views

"""
Using slug to uniquely identify users for hyperlinking to their profile.
"""

app_name = 'profiles'

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
]
