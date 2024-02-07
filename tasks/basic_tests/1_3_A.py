import random
import json

result = []

for i in range(10):
    inputs = [random.randint(0, 9), random.randint(0, 9)]

    result.append({"inputs": inputs, "outputs": [max(inputs[0], inputs[1])]})

with open("1_3_A.json", "w") as f:
    json.dump(result, f, indent=4)
