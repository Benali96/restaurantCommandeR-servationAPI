from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(arg='Repas.urls')),
        path('api/', include('order.urls')),
      path('api/', include('reservation.urls')),


    path('api/rest/', include('accounts.urls')),
     path('api/token/', TokenObtainPairView.as_view()),

]

