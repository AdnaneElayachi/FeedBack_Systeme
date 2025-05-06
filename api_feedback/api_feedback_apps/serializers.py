


from rest_framework import serializers
from rest_framework.views import APIView
from .models import FeedbackModel, HistoryEntry

class FeedbackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False}  # Rend le champ optionnel en mise à jour
        }

    def update(self, instance, validated_data):
        # Garde l'ancienne image si non fournie
        if 'image' not in validated_data:
            validated_data['image'] = instance.image
        return super().update(instance, validated_data)

class HistoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryEntry
        fields = '__all__'

class UpdateFeedbackAPIView(APIView):
    # Ajoutez ici la logique de votre vue
    pass