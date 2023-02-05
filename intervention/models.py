from django.db import models
from machine.models import Machine


class WorkCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    # REFACTOR (take out blank=True)
    machine = models.ForeignKey(Machine, on_delete=False, blank=True)
#  link to ServiceManager:
    case_created_by = models.CharField(max_length=255)  # to be reviewed
#  lint to customer
    customer_name = models.CharField(max_length=255)  # to be reviewed
#  move to Customer    customer_address = models.CharField(max_length=255)  # to be reviewed
    problem_description = models.TextField()  # to be reviewed
#  lint to Technician
    technician_assigned_id = models.CharField(max_length=255)  # to be reviewed
    time_case_create = models.TimeField(auto_now_add=True)
    time_case_edited = models.TimeField(auto_now=True)
# case_pdf = ???
