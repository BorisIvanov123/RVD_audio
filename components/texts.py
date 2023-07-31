import random

# Company Names
companies = ['Lufthansa', 'Speedbird','Air France', 'Turkish', 'Qatari', 'Austrian', 'Ryanair', 'Wizz Air', 'Flying Bulgaria', 'KLM']  # list of companies

# Flight Numbers
flight_numbers = random.sample(range(100, 1000), 20)
print(flight_numbers)

# Heading 
heading = ['Right', 'Left']

# Degrees
degrees = range(0, 361, 5)  # 0 to 360 with step 5
print(list(degrees))
# Speeds 
speeds = [100, 200]

# Altitudes
altitudes = [100, 200, 300]  # 100 to 300 with step 100

# Landing 
landing = ['cleared to land']

# Take Off
take_off = ['Cleared for takeoff']