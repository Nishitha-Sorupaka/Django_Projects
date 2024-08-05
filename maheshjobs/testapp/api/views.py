from rest_framework.viewsets import ModelViewSet
from testapp.models import HydJobs
from testapp.api.serializers import HydJobsSerializer
class HydJobsCRUDCBV(ModelViewSet):
    queryset = HydJobs.objects.all()
    serializer_class = HydJobsSerializer