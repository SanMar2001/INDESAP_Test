from django.utils import timezone
from rest_framework import serializers

from .models import Worker, WorkSession


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class WorkSessionSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)

    class Meta:
        model = WorkSession
        fields = ["id", "code", "worker", "start_time", "end_time", "total_time"]
        read_only_fields = ["id", "worker", "start_time", "end_time", "total_time"]

    def validate(self, data):
        code = data.get("code")

        try:
            worker = Worker.objects.get(code=code)
        except Worker.DoesNotExist:
            raise serializers.ValidationError("No se encontró al trabajador")

        active_session = WorkSession.objects.filter(
            worker=worker, end_time__isnull=True
        ).exists()

        if active_session:
            raise serializers.ValidationError(
                "El trabajador ya tiene una sesión activa"
            )

        data["worker"] = worker
        return data

    def create(self, validated_data):
        worker = validated_data.pop("worker")
        validated_data.pop("code", None)

        session = WorkSession.objects.create(worker=worker)

        return session


class EndSessionSerializer(serializers.Serializer):
    code = serializers.CharField()

    def validate(self, data):
        code = data["code"]

        try:
            worker = Worker.objects.get(code=code)
        except Worker.DoesNotExist:
            raise serializers.ValidationError("No se encontró al trabajador")

        try:
            session = WorkSession.objects.get(worker=worker, end_time__isnull=True)
        except WorkSession.DoesNotExist:
            raise serializers.ValidationError("No hay una sesión activa")

        data["session"] = session

        return data

    def save(self):
        session = self.validated_data["session"]
        session.end_time = timezone.now()
        session.total_time = session.end_time - session.start_time
        session.save()

        return session
