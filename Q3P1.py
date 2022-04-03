# Get an integer from user input
def get_str(prompt) -> str:
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("Invalid input!")
            continue
        # Valid input, exit loop
        else:
            break
    return value


def get_module_name(module_code: str):
    switch = {
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networks",
    }
    return switch.get(module_code, "Unknown module code!")


def main() -> None:
    code: str = get_str("Enter a module code:\n")
    name: str = get_module_name(code)
    print(name)


if __name__ == '__main__':
    main()
