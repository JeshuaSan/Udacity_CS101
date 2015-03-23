# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second
speed_of_light_ms = speed_of_light / 1000

def speed_fraction(ms, distance):
    speed = distance / (ms / 2.0)   # round trip
    fraction = speed / speed_of_light_ms
    return fraction


print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
