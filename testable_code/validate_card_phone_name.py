import sys

def main(card_number: str, phone_number: str, name: str):

    # Is credit card number valid?
    ccvalid = False
    if len(card_number) == 16:
        digits = [int(x) for x in str(card_number)]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum([int(x) for x in str(d*2)])

        if checksum % 10 == 0:
            ccvalid = True

    print("Card Validation Result:", ccvalid)

    # Is phone number valid and what type of number is it?
    phone_number_valid = False
    if phone_number.isdigit():
        if 9 <= len(phone_number) <= 11:
            phone_number_valid = True
    elif phone_number.startswith("+") and phone_number[1:].isdigit():
        if 9 <= len(phone_number)-1 <= 11:
            phone_number_valid = True

    print("Phone Validation Result:", phone_number_valid)

    name_valid = False
    if name.strip().replace(" ", "").isalpha():
        if len(name.split(" ")) == 2 and len(name) <= 20:
            name_valid = True

    print("Name Validation Result:", name_valid)

    return ccvalid, phone_number_valid, name_valid

if __name__ == "__main__":
    card_number = sys.argv[1]
    phone_number = sys.argv[2]
    name = sys.argv[3]
    print(card_number, phone_number, name)
    main(card_number, phone_number, name)
