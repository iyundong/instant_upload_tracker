from .models import IuPerfTracker, IuDeviceInfoTracker, IuBugTracker
from rest_framework import routers, serializers, viewsets

class IuPerfTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IuPerfTracker
        fields = '__all__'


class IuPerfTrackerViewSet(viewsets.ModelViewSet):
    queryset = IuPerfTracker.objects.all()
    serializer_class = IuPerfTrackerSerializer


class IuDeviceInfoTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IuDeviceInfoTracker
        fields = '__all__'

class IuDeviceInfoTrackerViewSet(viewsets.ModelViewSet):
    queryset = IuDeviceInfoTracker.objects.all()
    serializer_class = IuDeviceInfoTrackerSerializer

class IuBugTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IuBugTracker
        fields = '__all__'

class IuBugTrackerViewSet(viewsets.ModelViewSet):
    queryset = IuDeviceInfoTracker.objects.all()
    serializer_class = IuDeviceInfoTrackerSerializer

