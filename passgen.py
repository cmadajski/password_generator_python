import sys
from random import randint

def generate_password(length: int = 24) -> str:
    password = list()
    # determine placement of special char
    special_char_index = randint(0, length - 1)
    # iterator keeps track of while loop iterations
    iterator = 0
    # generate a unique char sequence
    while iterator < length:
        # special generator to ensure at least one special char
        if iterator == special_char_index:
            # generate a random number (11 outcomes for 11 special chars)
            rand_int = randint(0, 10)
            # convert ascii value to char
            char = int_to_special_char(rand_int)
            # add char to list
            password.append(char)
            # increment iterator
            iterator += 1
            # skip the rest of this iteration
            continue
        # generate a random number (62 alphanumeric char - 10 int, 26 upper, 26 lower)
        rand_int = randint(0, 61)
        # convert ascii value to char
        char = int_to_ascii(rand_int)
        # add char to list
        password.append(char)
        # increment iterator
        iterator += 1
    # convert list to string
    return "".join(password)

def int_to_ascii(num: int) -> str:
    ascii_value: int
    # 0 - 9 for numeric values
    if num <= 9:
        ascii_value = num + 48
    elif num <= 35:
        ascii_value = num + (65 - 10)
    else:
        ascii_value = num + (97 - 36)
    # convert ascii number to char
    return chr(ascii_value)

def int_to_special_char(num: int) -> str:
    ascii_value: int
    # 0 - 10 for special chars
    ascii_value = num + 33
    # convert ascii number to char
    return chr(ascii_value)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("ARG ERROR: To many args provided.")
    elif len(sys.argv) == 1:
        # use default 24 char length
        new_password = generate_password()
    else:
        new_password = generate_password(int(sys.argv[1]))
    print(new_password)