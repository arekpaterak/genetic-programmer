import random
import json

result = []

for i in range(10):
    inputs = [random.randint(-9, 9), random.randint(-9, 9)]

    result.append({"inputs": inputs, "outputs": [inputs[0] + inputs[1]]})

with open("1_2_B.json", "w") as f:
    json.dump(result, f, indent=4)
