from django.contrib import admin
from django.urls import path, include
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_server/', views.update, name='update'),
    path('api/auth/', include('accounts.urls')),
]