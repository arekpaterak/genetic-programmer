from src.generator.generator import Generator

if __name__ == "__main__":
    params = {
        "seed": None,
        # restricting the range of values of integers
        "int_min": -100,
        "int_max": 100,
        # controlling the use of floats and their range
        "use_floats": True,
        "float_min": -100.0,
        "float_max": 100.0,
        # choosing the method of generating the program
        "full_method": True,
        # controlling the size of the program
        "max_expression_size": 2,
        "max_program_depth": 2,
        "max_program_width": 2,
        "max_block_width": 2,
    }
    generator = Generator(params)
    # generator = Generator.from_config_file("src/configs/config.json")

    # for i in range(1):
    #     with open(f"generated_examples\{i}.txt", "w") as f:
    #         f.write(str(generator.generate_program()) + "\n")

    for _ in range(1):
        print(generator.generate_program())
