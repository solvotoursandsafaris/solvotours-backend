from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def health_check(request):
    return JsonResponse({"status": "Backend is working!", "service": "solvotours-backend"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),
    path('health/', health_check),
    # path('api/', include('safaris.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)