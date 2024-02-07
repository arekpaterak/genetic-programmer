import random
import json

result = []

for _ in range(10):
    inputs = [random.randint(-100, 100), random.randint(-100, 100)]

    outputs = [31415]

    result.append({"inputs": inputs, "outputs": outputs})

with open("1_1_C.json", "w") as f:
    json.dump(result, f, indent=4)
