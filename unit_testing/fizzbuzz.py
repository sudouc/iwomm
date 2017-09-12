def get_output(number: int) -> str:
    """
    Return the correct string to print for the number, following FizzBang rules
    """
    output = ""
    if number % 3 == 0:
        output += "Fizz"

    if number % 5 == 0:
         output += "Buzz"

    if not output:
        output = str(number)

    return output

if __name__ == "__main__":
    for i in range(1, 101):
        print(get_output(i))
