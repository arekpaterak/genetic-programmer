import numpy as np
import random
import json

result = []

for _ in range(10):
    inputs = [(n := random.randint(0, 99))] + [
        random.randint(-99, 99) for _ in range(n)
    ]

    result.append(
        {"inputs": inputs, "outputs": [round(np.mean(inputs[1 : inputs[0] + 1]))]}
    )

with open("1_4_B.json", "w") as f:
    json.dump(result, f, indent=4)
