from django.db import models


class HistoryEntry(models.Model):
    prediction = models.CharField(max_length=255)  # Prédiction
    confidence = models.FloatField()  # Confiance
    image = models.ImageField(upload_to='images/', default='default.jpg', null=False, blank=False)
    date = models.DateTimeField()  # Date associée à l'entrée
    latitude = models.FloatField()  # Latitude
    longitude = models.FloatField()  # Longitude

    def to_dict(self):
        return {
            'id': self.id,
            'prediction': self.prediction,
            'confidence': self.confidence,
            'image': self.image.url if self.image else None,
            'date': self.date.isoformat(),
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            prediction=data['prediction'],
            confidence=data['confidence'],
            image=data['image'],  # Assurez-vous que c'est une instance ou un chemin valide
            date=data['date'],
            latitude=data['latitude'],
            longitude=data['longitude'],
        )


class FeedbackModel(models.Model):
    predicted_class = models.CharField(max_length=255)  # Classe prédite
    suggested_class = models.CharField(max_length=255)  # Classe suggérée
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='feedback_images/')
    latitude = models.FloatField()  # Latitude
    longitude = models.FloatField()  # Longitude
    validated = models.BooleanField(default=False)  # Feedback validé ou non
    commentaire = models.TextField(null=True, blank=True)  # Commentaire optionnel

    class Meta:
        permissions = [
            ("can_validate_feedback", "Can validate feedback"),
        ]

    def to_dict(self):
        return {
            'id': self.id,
            'predictedClass': self.predicted_class,
            'suggestedClass': self.suggested_class,
            'date': self.date.isoformat(),
            'image': self.image.url if self.image else None,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'validated': self.validated,
            'commentaire': self.commentaire,
            }
    def validate_feedback(self):
        if not self.validated:
            if not self.image or not self.latitude or not self.longitude:
                raise ValueError("Le feedback doit contenir une image, une latitude et une longitude.")

            validated_image = ValidatedImage.objects.create(
                            feedback=self,
                name=f"Validated_{self.id}",  # Generate a unique name
                predicted_class=self.predicted_class,
                image=self.image,
                latitude=self.latitude,
                longitude=self.longitude,
                        )
            print(f"ValidatedImage created: {validated_image}")  # Debugging
            self.validated = True
            self.save()

    def __str__(self):
        return f"Feedback: {self.id}"

class ValidatedImage(models.Model):
    feedback = models.OneToOneField(
        'FeedbackModel',  # Reference to the FeedbackModel
        on_delete=models.CASCADE,
        related_name='validated_image',
        null=True,  # Allow null for backward compatibility
        blank=True  # Allow blank in forms
    )
    name = models.CharField(max_length=255, unique=True)
    predicted_class = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='validated_images/')
    validated_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"ValidatedImage: {self.id} (Feedback: {self.feedback.id if self.feedback else 'None'})"