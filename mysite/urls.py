
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("accounts.urls")),
    # path('',include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    # path('users/', auth_views..as_view(), name='admin:user-list'),
    
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  