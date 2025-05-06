import base64
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from api_feedback_apps.models import FeedbackModel
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

# ✅ Fixture pour le client API avec authentification
@pytest.fixture
@pytest.mark.django_db
def api_client():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpassword")
    client.force_authenticate(user=user)
    return client

# ✅ Fixture pour les données de test
@pytest.fixture
def feedback_data():
    image_data = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/1cAAwMBAATYHTIAAAAASUVORK5CYII="
    )
    image_file = SimpleUploadedFile("test_image.png", image_data, content_type="image/png")

    return {
        "predicted_class": "Cat",
        "suggested_class": "Dog",
        "image": image_file,
        "confidence": 0.95,
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-05-05T10:00:00Z",
    }

# ✅ Test pour créer une entrée de feedback
@pytest.mark.django_db
def test_create_feedback(api_client, feedback_data):
    url = reverse("feedbackmodel-list")
    response = api_client.post(url, feedback_data, format="multipart")
    assert response.status_code == 201

# ✅ Test pour récupérer la liste des feedbacks
@pytest.mark.django_db
def test_get_feedback_list(api_client, feedback_data):
    FeedbackModel.objects.create(**feedback_data)
    url = reverse("feedbackmodel-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
