Output = list[int | float | bool]


def value_present(actual_output: Output, target_output: Output) -> float:
    if len(actual_output) == 0:
        return -100000
    target_value = target_output[0]
    closest = min(actual_output, key=lambda x: abs(x - target_value))
    return -abs(closest - target_value)


def value_first(actual_output: Output, target_output: Output) -> float:
    if len(actual_output) == 0:
        return -100000
    target_value = target_output[0]
    return -abs(actual_output[0] - target_value)


def single_value(actual_output: Output, target_output: Output) -> float:
    if len(actual_output) == 0:
        return -100000

    target_value = target_output[0]
    if len(actual_output) == 1:
        return -abs(actual_output[0] - target_value)
    else:
        closest = min(actual_output, key=lambda x: abs(x - target_value))
        return len(actual_output) * (-abs(closest - target_value) - 1)


def exact_value(actual_output: Output, target_output: Output) -> float:
    if len(actual_output) == 0:
        return -10000

    target_value = target_output[0]
    if len(actual_output) == 1:
        return -10000 * (not (actual_output[0] == target_value))
    else:
        return -10000


if __name__ == "__main__":
    print(exact_value([True], [5]))
