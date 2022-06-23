from .models import Flight, Passenger, Reservation
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True, required=False)
    class Meta:
        model = Reservation
        fields = "__all__"
