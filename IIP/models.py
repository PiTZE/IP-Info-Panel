from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=100, blank=True)
    previous_ip = models.GenericIPAddressField(null=True, blank=True)
    current_ip = models.GenericIPAddressField()
    status = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name}, Previous IP: {self.previous_ip}, Current IP: {self.current_ip}, Status: {self.status}"
