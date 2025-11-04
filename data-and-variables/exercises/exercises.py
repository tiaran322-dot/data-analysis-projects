# 1. Declare and assign the variables here:

shuttle_name = 'Determination'
speed = 17500
dist_to_Mars = 225000000
dist_to_Moon = 384400
mpk = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(speed))
print(type(dist_to_Mars))
print(type(dist_to_Moon))
print(type(mpk))

# Code your solution to exercises 3 and 4 here:
miles_to_mars = dist_to_Mars * mpk

hours_to_mars = miles_to_mars / speed

Days_to_mars = hours_to_mars / 24

print(shuttle_name + " will take " + str(Days_to_mars) + " days to reach Mars")

# Code your solution to exercise 5 here
miles_to_moon = dist_to_Moon * mpk

hours_to_moon = miles_to_moon / speed

Days_to_moon = hours_to_moon / 24

print(shuttle_name + " will take " + str(Days_to_moon) + " days to reach the Moon")

