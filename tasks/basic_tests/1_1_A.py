import random
import json

result = []

for _ in range(10):
    inputs = [random.randint(0, 1000), random.randint(0, 1000)]

    outputs = [1]

    result.append({"inputs": inputs, "outputs": outputs})

with open("1_1_A.json", "w") as f:
    json.dump(result, f, indent=4)
