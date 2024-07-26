from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from productos import urls as productos_urls
from clientes import urls as clientes_urls
from ordenes import urls as ordenes_urls
from rest_framework.documentation import include_docs_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include(productos_urls)),
    path('clientes/', include(clientes_urls)),
    path('ordenes/', include(ordenes_urls)),
    path('docs/', include_docs_urls(title="Store API")),
    re_path('login', views.login),
    re_path('register', views.register),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
