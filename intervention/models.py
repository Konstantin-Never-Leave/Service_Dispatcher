from django.db import models


class WorkCase(models.Model):
    case_id = models.CharField(max_length=255)  # to be reviewed
    customer_name = models.CharField(max_length=255)  # move to customer model
    customer_address = models.CharField(max_length=255)  # move to customer model
    machine_id = models.CharField(max_length=255)
    # machine_type = models.CharField(max_length=255)  # move to machine model
    # machine_serial_number = models.CharField(max_length=255)  # move to machine model
    # machine_installation_year = models.CharField(max_length=255)  # move to machine model
    problem_description = models.CharField(max_length=255)  # to be reviewed
    technician_assigned_id = models.CharField(max_length=255)  # to be reviewed
