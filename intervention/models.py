from django.db import models


class WorkCase(models.Model):
    case_id = models.CharField(max_length=255)  # to be reviewed
    customer_name = models.CharField(max_length=255)  # to be reviewed
    customer_address = models.CharField(max_length=255)  # to be reviewed
    machine_type = models.CharField(max_length=255)  # to be reviewed
    machine_serial_number = models.CharField(max_length=255)  # to be reviewed
    machine_installation_year = models.CharField(max_length=255)  # to be reviewed
    problem_description = models.CharField(max_length=255)  # to be reviewed
    technician_assigned_id = models.CharField(max_length=255)  # to be reviewed
