from django.http import JsonResponse
from django.urls import reverse

def home(request):
    return JsonResponse({
        "message": "Welcome to RemindMe API 🚀",
        "endpoints": {
            "admin": request.build_absolute_uri(reverse("admin:index")),
            "register": request.build_absolute_uri("/api/register/"),
            "token_obtain": request.build_absolute_uri("/api/token/"),
            "token_refresh": request.build_absolute_uri("/api/token/refresh/"),
            "reminders": request.build_absolute_uri("/api/reminders/"),
        }
    })
