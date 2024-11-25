import requests


url = 'http://localhost:9696/predict'

customer = {
    "gender": "Male",
    "customer_type": "disloyal Customer",
    "age": 24,
    "type_of_travel": "Business travel",
    "class": "Business",
    "flight_distance": 351,
    "inflight_wifi_service": 5,
    "departure/arrival_time_convenient": 0,
    "ease_of_online_booking": 5,
    "gate_location": 1,
    "food_and_drink": 2,
    "online_boarding": 5,
    "seat_comfort": 2,
    "inflight_entertainment": 2,
    "on-board_service": 5,
    "leg_room_service": 2,
    "baggage_handling": 5,
    "checkin_service": 3,
    "inflight_service": 1,
    "cleanliness": 2,
    "departure_delay_in_minutes": 0,
    "arrival_delay_in_minutes": 0
 }

response = requests.post(url, json=customer).json()
print(response)
