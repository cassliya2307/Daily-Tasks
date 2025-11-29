def get_car_fuel_consumed(distance):
    fuel_efficiency = 15
    fuel_consumed = distance / fuel_efficiency
    return fuel_consumed

def refuel_tank(liters , fuel_remaining):
    if liters > 50 or liters + fuel_remaining > 50:
        return "Tank overflow"
    else:
        fuel_remaining = fuel_remaining + liters
        return fuel_remaining

def check_car_state(operation):
    if operation == "1":
        return "car is moving"
    else:
        return "car is not moving"

