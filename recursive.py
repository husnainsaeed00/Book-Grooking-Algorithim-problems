def count_number(num):
    if num == 0:
        return 0
    else:
        # Otherwise, it recursively calls the function with the integer division of the number by 10 
        # (to remove the rightmost digit) and adds 1 to the result.
        return 1 + count_number(num // 10)


def main():
    num = 12345
    result = count_number(num)
    print("Count:", result)


if __name__ == "__main__":
    main()
