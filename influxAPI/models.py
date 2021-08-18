from django.db import models


class Datas(models.Model):
    data = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time
