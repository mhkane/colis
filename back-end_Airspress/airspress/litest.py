from django.utils import timezone
import datetime
from trips.cstrips import trips

adata = timezone.now() + datetime.timedelta(days=3)
tripy = trip(departureDate=adata)
tripy.save()
