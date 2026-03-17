from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Worker
from .serializers import EndSessionSerializer, WorkerSerializer, WorkSessionSerializer


# Create your views here.
@api_view(["GET", "POST"])
def workers(request):

    if request.method == "GET":
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = WorkerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def start_session(request):
    serializer = WorkSessionSerializer(data=request.data)

    if serializer.is_valid():
        session = serializer.save()
        return Response(
            {"message": "Sesión iniciada", "session_id": session.id},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def end_session(request):
    serializer = EndSessionSerializer(data=request.data)

    if serializer.is_valid():
        session = serializer.save()
        return Response(
            {
                "message": "Sesión terminada",
                "session_id": session.worker.name,
                "total_time": session.total_time,
            },
            status=status.HTTP_200_OK,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
