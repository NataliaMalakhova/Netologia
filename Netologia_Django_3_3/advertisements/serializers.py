from rest_framework import serializers
from .models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'author']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def validate(self, data):
        # Проверка на количество открытых объявлений
        request = self.context['request']
        if data.get('status') == 'OPEN' and Advertisement.objects.filter(author=request.user, status='OPEN').count() >= 10:
            raise serializers.ValidationError("You can't have more than 10 open advertisements.")
        return data
