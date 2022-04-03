
def main() -> None:
    printStr = ""
    for x in range(102, 66, -1):
        if ((x & 1) == 1):
            printStr = printStr + str(x) + ", "
    printStr = printStr[:-2]
    print(printStr)


if __name__ == '__main__':
    main()
