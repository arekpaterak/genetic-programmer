import json


def generate_table():
    arguments = [False, True]
    table = []

    for a in arguments:
        for b in arguments:
            for c in arguments:
                for d in arguments:
                    for e in arguments:
                        inputs = [a, b, c, d, e]
                        output = a or b or c or d or e
                        entry = {"inputs": inputs, "outputs": [output]}
                        table.append(entry)

    return table


if __name__ == "__main__":
    table = generate_table()

    print(table)

    with open("k5_or.json", "w") as file:
        json.dump(table, file, indent=4)
