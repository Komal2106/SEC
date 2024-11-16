from django.urls import path
from .views import SimulationView, DecisionView, OutcomeView

urlpatterns = [
    path('', SimulationView.as_view()),
    path('decision/', DecisionView.as_view()),
    path('outcome/<int:simulation_id>/', OutcomeView.as_view()),
]
