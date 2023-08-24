import time
from math import pi
seconds = time.time()

current = time.ctime(seconds)
print(current)
print(pi)
angle = 32
angconv = angle/180 * pi
angconv = round(angconv,4)
print(f"{angconv}{'rad'}")

radius = int(input("Enter radius: "))
surarea = 4 * pi * (radius**2)
volume = 4/3 * pi * (radius**3)
surarea = str(surarea)
volume = str(volume)
print(f"{'Area of the sphere: '}{surarea}")
print(f"{'Volume of the sphere: '}{volume}")


sentence = str(input("Your sentence: "))
sentence = sentence.split()
print(sentence)

newSentence = ' '.join(sentence)
print(newSentence)