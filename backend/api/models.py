from django.db import models


# Create your models here.
class Worker(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkSession(models.Model):
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="sessions"
    )
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"Sesión de trabajo de: {self.worker.name} | ID: {self.id}"
