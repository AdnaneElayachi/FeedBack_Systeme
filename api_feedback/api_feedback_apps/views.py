# from django.shortcuts import get_object_or_404, render
# from fastapi import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response  # Correct import
# from rest_framework import status  # Correct import
# from .models import HistoryEntry, FeedbackModel, ValidatedImage
# from .serializers import HistoryEntrySerializer, FeedbackModelSerializer
# from django.contrib.auth.decorators import permission_required
# from django.http import HttpResponse
# from django.views.decorators.http import require_http_methods
# from rest_framework.decorators import api_view
# from django.http import HttpResponse, JsonResponse  # Avoid mixing these with DRF's Response



# class HistoryEntryViewSet(ModelViewSet):
#     queryset = HistoryEntry.objects.all()
#     serializer_class = HistoryEntrySerializer

# class FeedbackModelViewSet(ModelViewSet):
#     queryset = FeedbackModel.objects.all()
#     serializer_class = FeedbackModelSerializer


# @permission_required('app.change_feedback', raise_exception=True)
# def validate_feedback(request, feedback_id):
#     """
#     Vue pour valider un feedback spécifique.
#     """
#     feedback = get_object_or_404(FeedbackModel, id=feedback_id)
#     feedback.validated = True
#     feedback.save()
#     return HttpResponse(f"Feedback {feedback.id} validé avec succès.")


# @permission_required('app.view_feedback', raise_exception=True)
# def feedback_list(request):
#     """
#     Vue pour afficher la liste des feedbacks non validés.
#     """
#     feedbacks = FeedbackModel.objects.filter(validated=False)
#     return render(request, 'feedback_list.html', {'feedbacks': feedbacks})




# import base64
# import uuid
# from django.core.files.base import ContentFile
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import FeedbackModelSerializer


# @api_view(['POST'])
# def receive_feedback(request):
#     data = request.data.copy()

#     # Récupérer le champ imageBase64
#     image_base64 = data.get('imageBase64')

#     if image_base64:
#         try:
#             # Décoder le base64
#             format, imgstr = image_base64.split(';base64,') if ';base64,' in image_base64 else (None, image_base64)
#             ext = format.split('/')[-1] if format else 'png'
#             file_name = f"{uuid.uuid4()}.{ext}"

#             # Créer un fichier Django depuis le base64
#             data['image'] = ContentFile(base64.b64decode(imgstr), name=file_name)
#         except Exception as e:
#             return Response({"error": f"Erreur décodage base64 : {str(e)}"}, status=400)

#     # Enlever le champ imageBase64 pour ne pas perturber la validation
#     data.pop('imageBase64', None)

#     serializer = FeedbackModelSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Feedback reçu avec succès", "feedback": serializer.data}, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def receive_history(request):
#     data = request.data.copy()

#     # Récupérer le champ imageBase64
#     image_base64 = data.get('imageBase64')

#     if image_base64:
#         try:
#             # Décoder le base64
#             format, imgstr = image_base64.split(';base64,') if ';base64,' in image_base64 else (None, image_base64)
#             ext = format.split('/')[-1] if format else 'png'
#             file_name = f"{uuid.uuid4()}.{ext}"

#             # Créer un fichier Django depuis le base64
#             data['image'] = ContentFile(base64.b64decode(imgstr), name=file_name)
#         except Exception as e:
#             return Response({"error": f"Erreur décodage base64 : {str(e)}"}, status=400)

#     # Enlever le champ imageBase64 pour ne pas perturber la validation
#     data.pop('imageBase64', None)

#     serializer = FeedbackModelSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Feedback reçu avec succès", "feedback": serializer.data}, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.base import ContentFile
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
import uuid

from .models import HistoryEntry, FeedbackModel, ValidatedImage
from .serializers import HistoryEntrySerializer, FeedbackModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated



# ViewSets
class HistoryEntryViewSet(ModelViewSet):
    queryset = HistoryEntry.objects.all()
    serializer_class = HistoryEntrySerializer


class FeedbackModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackModelSerializer
    permission_classes = [AllowAny]  # Désactiver les permissions pour les tests


# Feedback validation view@permission_required('app.change_feedback', raise_exception=True)
def validate_feedback(request, feedback_id):
    feedback = get_object_or_404(FeedbackModel, id=feedback_id)
    try:
        feedback.validate_feedback()
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=400)
    



@api_view(['POST'])
def validate_all_feedbacks(request):
    feedbacks = FeedbackModel.objects.filter(validated=False)
    result = {"validated": [], "errors": []}

    for feedback in feedbacks:
        try:
            feedback.validate_feedback()
            result["validated"].append(feedback.id)
        except Exception as e:
            result["errors"].append({"feedback_id": feedback.id, "error": str(e)})

    return Response(result)



# Feedback list view
@permission_required('app.view_feedback', raise_exception=True)
def feedback_list(request):
    """
    View to display a list of unvalidated feedbacks.
    """
    feedbacks = FeedbackModel.objects.filter(validated=False)
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})


# Helper function for processing base64 image
def process_base64_image(image_base64):
    if image_base64:
        try:
            # Decode base64
            format, imgstr = image_base64.split(';base64,') if ';base64,' in image_base64 else (None, image_base64)
            ext = format.split('/')[-1] if format else 'png'
            file_name = f"{uuid.uuid4()}.{ext}"
            return ContentFile(base64.b64decode(imgstr), name=file_name)
        except Exception as e:
            raise ValueError(f"Base64 decoding error: {str(e)}")
    return None


# Receive feedback
@api_view(['POST'])
def receive_feedback(request):
    data = request.data.copy()

    # Process base64 image if provided
    image_base64 = data.pop('imageBase64', None)
    if image_base64:
        try:
            data['image'] = process_base64_image(image_base64)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    serializer = FeedbackModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Feedback received successfully", "feedback": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Receive history
@api_view(['POST'])
def receive_history(request):
    data = request.data.copy()

    # Process base64 image if provided
    image_base64 = data.pop('imageBase64', None)
    if image_base64:
        try:
            data['image'] = process_base64_image(image_base64)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    serializer = HistoryEntrySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "History received successfully", "history": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def check_host_view(request):
    return HttpResponse(f"HTTP_HOST reçu : {request.get_host()}")