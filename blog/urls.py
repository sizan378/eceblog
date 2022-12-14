from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

...

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    # app path
    path('api/v1/notice/', include('apps.notice.urls')),
    path('api/v1/post/', include('apps.post.urls')),
    path('api/v1/userprofile/', include('apps.userprofile.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/comments/', include('apps.comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
