from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pages import views


urlpatterns = []


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),

    path('pages/', include('pages.urls', namespace='pages')),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),

    path('', views.HomeView.as_view(), name='home')
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)