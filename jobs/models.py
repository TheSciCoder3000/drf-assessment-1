from django.db import models


class Job(models.Model):
    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
