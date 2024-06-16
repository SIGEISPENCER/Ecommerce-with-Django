from django.contrib import admin
from django.urls import path, include

# Register your models here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ECOMMERCE/', include('ecommerce.urls')),  # Ensure this line is present
]