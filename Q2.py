
# Get an integer from user input
def get_int(prompt) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input!")
            continue
        # Valid input, exit loop
        else:
            break
    return value


# Get the average of a list of numbers
def get_average(list: list[int]) -> float:
    return sum(list) / len(list)


def main() -> None:
    x: int = get_int("Enter an integer value for x:\n")
    y: int = get_int("Enter an integer value for y:\n")
    average: float = get_average([x, y])
    print(f"The average of x and y is {average}")


if __name__ == '__main__':
    main()
