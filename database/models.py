from django.db import models
from django.contrib.postgres.fields import JSONField

SHORT_LENGTH = 100
LONG_LENGTH = 2000
DECIMAL_PLACES = 2
MAX_DIGITS = 10


class Farm(models.Model):
    """
    This class describes the profile of the farm.
    """
    farm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH, blank=True)
    bio = models.CharField(max_length=LONG_LENGTH)
    area = models.DecimalField(
        decimal_places=DECIMAL_PLACES, max_digits=MAX_DIGITS)  # in acres
    location = JSONField()  # json of {longitude, latitude}
    crops_grown = JSONField()  # json of {list of crop ids}
    interested_in_selling = models.BooleanField()
    # json of {person of contact name, phone, email}
    contact = JSONField()


class CropFamily(models.Model):

    """
    This table contains the general name of the crop

    """

    family_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    icon = models.CharField(max_length=LONG_LENGTH)


class Crop(models.Model):

    """

    This table will represent each crop

    """

    crop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    start_month = models.IntegerField()
    end_month = models.IntegerField()
    family_id = models.ForeignKey(
        CropFamily, blank=True, null=True, on_delete=models.SET_NULL)


class Month(models.Model):

    """
    This table stores all the months in a year
    """

    month_id_pk = models.AutoField(primary_key=True)
    crop_id_fk = models.ForeignKey(
        Crop, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=SHORT_LENGTH)
    month_number = models.IntegerField()


class Disease(models.Model):

    """
    This table contains all possible diseases
    """

    disease_id_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    picture_link = models.CharField(max_length=LONG_LENGTH)
    symptoms = JSONField()
    crops_affected = JSONField()  # json of {Secondary keys of crops}
    treatment = JSONField()  # json of {organic:, pesticide:}
