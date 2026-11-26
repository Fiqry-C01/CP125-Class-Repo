# Lab 01 Exercise 2: Camping Logistics
def calculate_tent_cost (participants,tent_capacity,tent_price):
    if participants % 2 != 0:
        tent_amount = (participants // tent_capacity) + 1
    else:
        tent_amount = participants / tent_capacity
    total = tent_price * tent_amount
    return (int(total))
print(calculate_tent_cost(12,4,100))
print(calculate_tent_cost(13,4,100))
