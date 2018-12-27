from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('quote.urls')),
    path('admin/', admin.site.urls),
]
