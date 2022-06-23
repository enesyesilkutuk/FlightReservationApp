from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, ReservationSerializer
from rest_framework import viewsets
from .permissions import IsStafforReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
