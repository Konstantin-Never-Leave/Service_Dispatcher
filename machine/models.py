from django.db import models
from django.utils.text import slugify


class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_serial_number = models.CharField(max_length=255, unique=True)
# link to MachineType:
    machine_type = models.CharField(max_length=255)  # to be reviewed
    machine_installation_year = models.CharField(max_length=255)  # to be reviewed
# link to WorkCase:
    machine_intervention = models.CharField(max_length=255)  # to be reviewed
# link to MachineOptionList:
    machine_option_list = models.CharField(max_length=255)  # to be reviewed
    machine_slug = models.TextField()

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        self.slug = slugify(self.machine_serial_number)
        super().save()


class MachineType(models.Model):
    machine_type_id = models.AutoField(primary_key=True)
    machine_type_name = models.CharField(max_length=255)


class MachineOptionList(models.Model):
    option_id = models.AutoField(primary_key=True)
    EU_US = models.CharField(max_length=255)  # to be reviewed
    length_x = models.CharField(max_length=255)  # to be reviewed
    head_list = models.CharField(max_length=255)  # to be reviewed
    table = models.CharField(max_length=255)  # to be reviewed

