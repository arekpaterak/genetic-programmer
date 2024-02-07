import numpy as np
import random
import json

result = []

for i in range(10):
    inputs = [random.randint(-99, 99) for i in range(15)]

    result.append({"inputs": inputs, "outputs": [round(np.mean(inputs[:10]))]})

with open("1_4_A.json", "w") as f:
    json.dump(result, f, indent=4)
