from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['created_at']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user != instance.author and not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to delete this advertisement.")
        instance.delete()

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_ads(self, request):
        my_ads = Advertisement.objects.filter(author=request.user)
        serializer = self.get_serializer(my_ads, many=True)
        return Response(serializer.data)
