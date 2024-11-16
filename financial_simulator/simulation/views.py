from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Simulation, Decision, Outcome
from .serializers import SimulationSerializer, DecisionSerializer, OutcomeSerializer

class SimulationView(APIView):
    def get(self, request):
        simulations = Simulation.objects.all()
        serializer = SimulationSerializer(simulations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SimulationSerializer(data=request.data)
        if serializer.is_valid():
            simulation = serializer.save()
            return Response(SimulationSerializer(simulation).data)
        return Response(serializer.errors, status=400)

class DecisionView(APIView):
    
    def get(self, request):
        decisions = Decision.objects.all()
        serializer = DecisionSerializer(decisions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DecisionSerializer(data=request.data)
        if serializer.is_valid():
            decision = serializer.save()
            return Response(DecisionSerializer(decision).data)
        return Response(serializer.errors, status=400)

class OutcomeView(APIView):
    def get(self, request, simulation_id):
        outcomes = Outcome.objects.filter(simulation_id=simulation_id)
        serializer = OutcomeSerializer(outcomes, many=True)
        return Response(serializer.data)
