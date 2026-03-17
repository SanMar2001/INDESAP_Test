from django.urls import path

from .views import end_session, start_session, workers

urlpatterns = [
    path("workers/", workers),
    path("start/", start_session),
    path("end/", end_session),
]
