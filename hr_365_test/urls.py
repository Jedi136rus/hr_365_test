from django.contrib import admin
from django.urls import path, include, re_path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('currency_converter.urls'))
]

# urlpatterns += [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
