from rest_framework.serializers import ModelSerializer
from testapp.models import *
class HydJobsSerializer(ModelSerializer):
    class Meta:
        model = HydJobs
        fields = '__all__'