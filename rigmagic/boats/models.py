from django.db import models

# Create your models here.

class Boat(models.Model):
    """The Model representing a boat.

       Make: Beneteau, Jeanneau, etc.
       Model: Oceanis, Sun Odyssey, etc.
       Type: 40.1, 45.2, etc.
       Variant: CWS, DS, etc.

    """
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100,null=True, blank=True)
    variant = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.type} {self.variant}"

class SailData(models.Model):
    """The Model representing the sail data for a boat.
       i:  The height of the foretriangle down to the deck 
       j:  Measured from the front of the mast to the point where the forestay meets the deck
       p:  Mainsail luff length measured from the top of the mast to the point where the sail meets the boom, or between the black bands if present
       e:  Mainsail foot length measured from the back face of the mast to the maximum outboard point of the boom, or between the black bands if present

       Mizzen measurements: (if applicable)
       mizzen: BOOL true/false
       mp: Mainsail area
       me: Jib area

       Imperial or Metric:  The units of measurement used for the boat.  This is important for the calculations.

    """
    boat = models.OneToOneField(Boat, on_delete=models.CASCADE)
    i = models.FloatField(null=True, blank=True)
    j = models.FloatField(null=True, blank=True)
    p = models.FloatField(null=True, blank=True)
    e = models.FloatField(null=True, blank=True)
    mizzen = models.BooleanField(default=False)
    mp = models.FloatField(null=True, blank=True)
    me = models.FloatField(null=True, blank=True)
    imperial_or_metric = models.CharField(choices=[('imperial', 'Imperial'), ('metric', 'Metric')], max_length=10, default='imperial')

    def __str__(self):
        return f"Sail Data for {self.boat.make} {self.boat.model} {self.boat.type} {self.boat.variant}"
