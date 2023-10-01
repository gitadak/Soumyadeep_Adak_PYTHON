#Generate the frequency of occurrence of each faces when a die is rolled 10000 times
import random

num_rolls = 10000
face_frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(num_rolls):
    roll = random.randint(1, 6)
    face_frequency[roll] += 1

for face, frequency in face_frequency.items():
    print(f"Face {face}: {frequency} times ({(frequency / num_rolls) * 100:.2f}% frequency)")