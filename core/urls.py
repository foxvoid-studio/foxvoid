import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("public.urls")),
    path('games/', include("games.urls")),
    path('auth/', include("authentication.urls")),
    prefix_default_language=False
)

if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += [
            path('rosetta/', include('rosetta.urls')),
        ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
