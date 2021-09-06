from django.urls import path, include
from .routers import router

urlpatterns = [
    path('apis-mhl/', include(router.urls)),
    
]