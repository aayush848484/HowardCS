from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
from machina.app import board

# Events
# MarketPlace
# Spotlight
# Forum
# About


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^forum/', include(board.urls)),
    url(r'^events/', include('event_rsvp.urls', namespace='event_rsvp'))
]

# Static files such as user-profile photo to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# If django Debug is True, add the debug toolbar for convenience.
"""
if not settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
"""