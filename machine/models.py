from django.db import models


class Machine(models.Model):
    machine_id = models.CharField(max_length=255)  # to be reviewed
    machine_serial_number = models.CharField(max_length=255)  # to be reviewed
# link to MachineType:
    machine_type = models.CharField(max_length=255)  # to be reviewed
    machine_installation_year = models.CharField(max_length=255)  # to be reviewed
# link to WorkCase:
    machine_intervention = models.CharField(max_length=255)  # to be reviewed
# link to MachineOptionList:
    machine_option_list = models.CharField(max_length=255)  # to be reviewed


class MachineType(models.Model):
    pass


class MachineOptionList(models.Model):
    pass
