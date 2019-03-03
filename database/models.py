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
    name = models.CharField(max_length=SHORT_LENGTH)
    bio = models.TextField(max_length=LONG_LENGTH, blank=True, null=True)
    area = models.DecimalField(
        decimal_places=DECIMAL_PLACES, max_digits=MAX_DIGITS)  # in acres
    location = JSONField()  # json of {longitude, latitude}
    crops_grown = JSONField()  # json of {list of crop ids}
    interested_in_selling = models.BooleanField(default=False)
    # json of {person of contact name, phone, email}
    contact = JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Farms"


class CropFamily(models.Model):

    """
    This table contains the general name of the crop

    """

    family_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH, unique=True)
    icon = models.CharField(max_length=LONG_LENGTH)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Crops"


class Crop(models.Model):

    """

    This table will represent each crop

    """

    crop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH, unique=True)
    start_month = JSONField()
    end_month = JSONField()
    family_id = models.ForeignKey(
        CropFamily, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Varieties"


class Disease(models.Model):

    """
    This table contains all possible diseases
    """

    disease_id_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    common_name = models.CharField(
        max_length=SHORT_LENGTH, blank=True, null=True)
    picture_link = models.CharField(max_length=LONG_LENGTH)
    symptoms = JSONField()
    crops_affected = JSONField()  # json of {Secondary keys of crops}
    treatment = JSONField()  # json of {organic:, pesticide:}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Diseases"


class Insect(models.Model):

    """
    This table contains all possible diseases
    """

    insect_id_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    common_name = models.CharField(
        max_length=SHORT_LENGTH, blank=True, null=True)
    picture_link = models.CharField(max_length=LONG_LENGTH)
    symptoms = JSONField()
    crops_affected = JSONField()  # json of {Secondary keys of crops}
    treatment = JSONField()  # json of {organic:, pesticide:}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Insects"


class ThreatType(models.Model):
    name = models.CharField(max_length=SHORT_LENGTH, unique=True)
    severity = models.CharField(max_length=SHORT_LENGTH)
    source = models.CharField(max_length=SHORT_LENGTH, blank=True, null=True)
    description = models.TextField(
        max_length=LONG_LENGTH, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types of Threats"


class Alert(models.Model):
    """
    """
    threat_level = models.CharField(max_length=SHORT_LENGTH)
    farm_associated = models.ForeignKey(
        Farm, blank=True, null=True, on_delete=models.SET_NULL)
    catalog_category = models.ForeignKey(
        Disease, blank=True, null=True, on_delete=models.SET_NULL)
    threat_type = models.ForeignKey(
        ThreatType, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=SHORT_LENGTH)

    def __str__(self):
        return self.threat_level

    class Meta:
        verbose_name_plural = "Alerts or Posts"


class Image(models.Model):
    name = models.CharField(max_length=SHORT_LENGTH, unique=True)
    description = models.TextField(max_length=LONG_LENGTH)
    picture = models.FileField(
        upload_to='uploads/', blank=True, null=True)
    disease_associated = models.ForeignKey(
        Disease, blank=True, null=True, on_delete=models.SET_NULL)
    alert_associated = models.ForeignKey(
        Alert, blank=True, null=True, on_delete=models.SET_NULL)
    crop_associated = models.ForeignKey(
        Crop, blank=True, null=True, on_delete=models.SET_NULL)
    crop_family_associated = models.ForeignKey(
        CropFamily, blank=True, null=True, on_delete=models.SET_NULL)
    farm_associated = models.ForeignKey(
        Farm, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Images"
