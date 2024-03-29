# -*- coding: utf-8 -*-
"""Assignment-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ADCS0oUn8HgBQzvbK2R3rVjpW5cHAXC
"""

# A class representing a passenger
class Passenger:
    # Constructor with basic passenger information
    def __init__(self, name, booking_reference):
        self.name = name
        self.booking_reference = booking_reference
        self.seat_preference = None  # Initialized as None, can be set later
        self.meal_preference = None  # Initialized as None, can be set later
        self.boarding_pass = None  # Will be linked to a BoardingPass object later

    # Getter method for passenger's name
    def get_name(self):
        return self.name

    # Setter method for passenger's name
    def set_name(self, name):
        self.name = name

    # Getter method for passenger's booking reference
    def get_booking_reference(self):
        return self.booking_reference

    # Setter method for passenger's booking reference
    def set_booking_reference(self, booking_reference):
        self.booking_reference = booking_reference

    # Getter method for passenger's seat preference
    def get_seat_preference(self):
        return self.seat_preference

    # Setter method for passenger's seat preference
    def set_seat_preference(self, seat_preference):
        self.seat_preference = seat_preference

    # Getter method for passenger's meal preference
    def get_meal_preference(self):
        return self.meal_preference

    # Setter method for passenger's meal preference
    def set_meal_preference(self, meal_preference):
        self.meal_preference = meal_preference

    # Getter method for passenger's boarding pass
    def get_boarding_pass(self):
        return self.boarding_pass

    # Setter method for linking a boarding pass to the passenger
    def set_boarding_pass(self, boarding_pass):
        self.boarding_pass = boarding_pass

# A Class representing a flight
class Flight:
    # Constructor with flight details
    def __init__(self, flight_number, departure, arrival, date, time):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.time = time


# Class representing a boarding pass
class BoardingPass:
    # Constructor with boarding pass details
    def __init__(self, passenger, flight, seat, gate, boarding_time, terminal):
        self.passenger = passenger  # Link to the Passenger object
        self.flight = flight        # Link to the Flight object
        self.seat = seat            # Assigned seat for the passenger
        self.gate = gate            # Departure gate for the flight
        self.boarding_time = boarding_time  # Time until which passenger can board
        self.terminal = terminal    # Terminal number at the airport
        self.barcode = "1234567890" # Placeholder for barcode value


#A Class representing the airline's system
class AirlineSystem:
    # Constructor for the airline system which will manage all objects
    def __init__(self):
        self.passengers = []  # List to store Passenger objects
        self.flights = []     # List to store Flight objects



# Instantiate objects with sample data from the boarding pass in the figure of assignment descriptions
passenger = Passenger("JAMES SMITH", "5A6BCD78")
flight = Flight("NA4321", "CHICAGO ORD", "NEW YORK JFK", "06 DEC 20", "11:40")
boarding_pass = BoardingPass(passenger, flight, "09A", "03", "11:20", "2")

# Use the objects' functions to display the boarding pass details
print("Boarding Pass Details:")
print(f"Passenger: {passenger.get_name()}")
print(f"From: {flight.departure}")
print(f"To: {flight.arrival}")
print(f"Flight: {flight.flight_number}")
print(f"Date: {flight.date}")
print(f"Time: {flight.time}")
print(f"Gate: {boarding_pass.gate}")
print(f"Boarding till: {boarding_pass.boarding_time}")
print(f"Seat: {boarding_pass.seat}")
print(f"Terminal: {boarding_pass.terminal}")
print(f"Electronic ticket number: {passenger.get_booking_reference()}")
print(f"Barcode: {boarding_pass.barcode}")

