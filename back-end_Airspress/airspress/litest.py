from django.utils import timezone
import datetime
from signup.trips import trip

adata = timezone.now() + datetime.timedelta(days=3)
tripy = trip(departureDate=adata)
tripy.save()