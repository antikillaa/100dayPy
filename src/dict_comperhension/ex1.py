sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")

result = {key: len(key) for key in words}


print(result)
