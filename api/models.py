from django.db import models


class Query(models.Model):
    domain = models.CharField(max_length=255)
    ipv4_addresses = models.JSONField()  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Query(domain={self.domain}, timestamp={self.timestamp})"
