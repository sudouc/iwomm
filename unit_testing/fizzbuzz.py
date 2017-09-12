def get_output(number: int) -> str:
    """
    Return the correct string to print for the number, following FizzBang rules
    """
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 5 ==0 and number % 3 == 0:
        return "FizzBang"
    else:
        return number

if __name__ == "__main__":
    for i in range(1, 101):
        print(get_output(i))
