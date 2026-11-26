# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric" :
        total = 2
    elif vehicle_type == "Hybrid":
        if (hour >= 22 and hour <= 23) or (hour >= 0 and hour <= 6):
            total = 2
        else:
            total = 5
    else:
        total = 5
    return(f"{total:.2f}")
print (get_hourly_rate("Hybrid", 23))
print (get_hourly_rate("Hybrid", 13))
print (get_hourly_rate("Sedan", 2))

