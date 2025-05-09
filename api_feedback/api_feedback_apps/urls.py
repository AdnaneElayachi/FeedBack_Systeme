from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HistoryEntryViewSet, FeedbackModelViewSet, check_host_view
from api_feedback_apps import views

router = DefaultRouter()
router.register(r'history_entries', HistoryEntryViewSet, basename='historyentry')
router.register(r'feedbacks', FeedbackModelViewSet, basename='feedbackmodel')

urlpatterns = router.urls + [
    path('validate-feedback/<int:feedback_id>/', views.validate_feedback, name='validate_feedback'),
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('receive_feedback/', views.receive_feedback, name='receive_feedback'),
    path('receive_history/', views.receive_history, name='receive_history'),
      path("check-host/", check_host_view),
]

