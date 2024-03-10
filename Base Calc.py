#1-function-from-dec-to-bin
def decimal_to_binary(decimal_num):
    binary_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num //= 2
    return binary_result if binary_result else "0"
#2-function-from-dec-to-oct
def decimal_to_octal(decimal_num):
    octal_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_result = str(remainder) + octal_result
        decimal_num //= 8
    return octal_result if octal_result else "0"
#3-function-from-dec-to-hex
def decimal_to_hexadecimal(decimal_num):
    hexadecimal_result = ""
    hex_digits = "0123456789ABCDEF"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_result = hex_digits[remainder] + hexadecimal_result
        decimal_num //= 16
    return hexadecimal_result if hexadecimal_result else "0"
#4-function-from-bin-to-dec
def binary_to_decimal(binary_num):
    decimal_result = 0
    binary_num = binary_num[::-1]  #5-Reverse the binary string for easier processing
    for i, digit in enumerate(binary_num):
        decimal_result += int(digit) * (2 ** i)
    return decimal_result
#6-function-from-oct-to-dec
def octal_to_decimal(octal_num):
    decimal_result = 0
    octal_num = octal_num[::-1]  #7-Reverse the octal string for easier processing
    for i, digit in enumerate(octal_num):
        decimal_result += int(digit) * (8 ** i)
    return decimal_result
#8-function-from-hex-to-dec
def hexadecimal_to_decimal(hexadecimal_num):
    decimal_result = 0
    hex_digits = "0123456789ABCDEF"
    hexadecimal_num = hexadecimal_num[::-1]  #9-Reverse the hexadecimal string for easier processing
    for i, digit in enumerate(hexadecimal_num.upper()):
        decimal_result += hex_digits.index(digit) * (16 ** i)
    return decimal_result
#10-function-for validation
def is_valid_number(user_number, base):
    try:
        if base == "A":
            int(user_number)
        elif base == "B":
            int(user_number, 2)
        elif base == "C":
            int(user_number, 8)
        elif base == "D":
            int(user_number, 16)
        return True
    except ValueError:
        return False
#11-converting-function
def convert_number():
    while True:
        print("Numbering System Converter")
        print("A) Insert a new number")
        print("B) Exit program")

        choice_menu1 = input("Enter your choice (A/B): ").upper()#built-in function in case the user input was lower case

        if choice_menu1 == "A":
            user_number = input("Please insert a number: ")

            print("Menu 2")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")

            choice_menu2 = input("Select the base you want to convert from (A/B/C/D): ").upper()

            if choice_menu2 in ["A", "B", "C", "D"]:
                if is_valid_number(user_number, choice_menu2):
                    print("Menu 3")
                    print("A) Decimal")
                    print("B) Binary")
                    print("C) Octal")
                    print("D) Hexadecimal")

                    choice_menu3 = input("Select the base you want to convert to (A/B/C/D): ").upper()

                    if choice_menu3 in ["A", "B", "C", "D"]:
                        try:
                            if choice_menu2 == "A":
                                decimal_number = int(user_number)
                            elif choice_menu2 == "B":
                                decimal_number = binary_to_decimal(user_number)
                            elif choice_menu2 == "C":
                                decimal_number = octal_to_decimal(user_number)
                            elif choice_menu2 == "D":
                                decimal_number = hexadecimal_to_decimal(user_number)

                            if choice_menu3 == "A":
                                 result = decimal_number
                            elif choice_menu3 == "B":
                                result = decimal_to_binary(decimal_number)
                            elif choice_menu3 == "C":
                                result = decimal_to_octal(decimal_number)
                            elif choice_menu3 == "D":
                                result = decimal_to_hexadecimal(decimal_number)

                            print("Result:", result)

                        except ValueError:
                            print("Error: Invalid input during convers.ion.")
                    else:
                        print("Error: Please select a valid choice.")
                else:
                    print("Error: Invalid number for the selected base. Please enter a valid number.")
            else:
                print("Error: Please select a valid choice.")
        elif choice_menu1 == "B":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Error: Please select a valid choice.")

convert_number()


# Ali Osama Ali                    id 20231108
# Asmaa Hassan Mohamed             id 20220850
# Abdelrahman Khaled Elhassan      id 20220990