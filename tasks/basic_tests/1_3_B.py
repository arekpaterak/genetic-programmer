import random
import json

result = []

for i in range(10):
    BOUNDS = [-9999, 9999]
    inputs = [
        random.randint(BOUNDS[0], BOUNDS[1]),
        random.randint(BOUNDS[0], BOUNDS[1]),
    ]

    result.append({"inputs": inputs, "outputs": [max(inputs[0], inputs[1])]})

with open("1_3_B.json", "w") as f:
    json.dump(result, f, indent=4)

#%%
