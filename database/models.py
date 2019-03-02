from django.db import models

SHORT_LENGTH = 100
LONG_LENGTH = 2000



class Farm(models.Model):

	"""
        This class describes the profile of the farm.  
    """

    farm_id_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH, blank=True)
    bio = models.CharField(max_length=LONG_LENGTH)
    area = models.DecimalField() #in acres
    location = models.JSONField() #json of {longitude, latitude}
    crops_grown = models.JSONField() #json of {list of crop ids}
    interested_in_selling = models.BooleanField()
    contact = models.JSONField() #json of {person of contact name, phone, email}


class Crop(models.Model):

    """

    This table will represent each crop

    """

    crop_id_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=SHORT_LENGTH)
    start_month = models.IntegerField()
    end_month = models.IntegerField()
    family_id_fk = models.ForeignKey(CropFamily, blank=True, null=True, on_delete=models.SET_NULL)



class CropFamily(models.Model):

	"""
	This table contains the general name of the crop

	"""

	family_id_pk = models.AutoField(primary_key=True)
	name = models.CharField(max_length=SHORT_LENGTH)
	icon = models.CharField(max_length=LONG_LENGTH)


class Month(models.Model):

	"""
	This table stores all the months in a year
	"""

	month_id_pk = models.AutoField(primary_key=True)
	crop_id_fk = models.ForeignKey(Crop, blank=True, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=SHORT_LENGTH)
	month_number = models.IntegerField()


class Disease(models.Model):

	"""
	This table contains all possible diseases
	"""

	disease_id_pk = models.AutoField(primary_key=True)
	name = models.CharField(max_length=SHORT_LENGTH)
	picture_link = models.CharField(max_length=LONG_LENGTH)
	symptoms = models.JSONField()
	crops_affected = models.JSONField() #json of {Secondary keys of crops}
	treatment = models.JSONField() #json of {organic:, pesticide:}
