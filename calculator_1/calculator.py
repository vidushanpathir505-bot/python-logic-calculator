import math

print("🧮 Welcome to Simple Calculator!")

# //-----------------\\


def addition(a, b):
    return a + b


# //-----------------\\


def subtraction(a, b):
    return a - b


# //-----------------\\


def multiplication(a, b):
    return a * b


# //-----------------\\


def division(a, b):
    # Handle division by zero
    if b == 0:
        return "🟡Cannot divide by zero🟡"

    return a / b


# //-----------------\\


def power(a, b):
    return a**b


# //-----------------\\


def sqrt(a):
    # Handle negative number sqrt
    if a < 0:
        return "🟡Cannot take squre root of negative number🟡"

    return math.sqrt(a)


# //-----------------\\


def get_valid_input():
    while True:
        try:
            number = float(input("Enter your number: "))
            return number
        except ValueError:
            print("🔴Enter Valid Number🔴")


# //-----------------\\


def main():

    while True:
        operation = input("choose the operator (+,-,*,/,**,sqrt): ")

        if operation == "sqrt":
            number = get_valid_input()

            answer = sqrt(number)

            print("-------------")
            print(f"Answer: {answer}")
            print("-------------")

        elif operation == "**":
            print("🟢Enter your Number🟢")
            number_1 = get_valid_input()

            print("🟢Enter your power🟢")
            number_2 = get_valid_input()

            answer = power(number_1, number_2)

            print("-------------")
            print(f"Answer: {answer}")
            print("-------------")

        elif (
            operation == "+" or operation == "-" or operation == "/" or operation == "*"
        ):
            number_1 = get_valid_input()
            number_2 = get_valid_input()

            if operation == "+":
                answer = addition(number_1, number_2)

                print("-------------")
                print(f"Answer: {answer}")
                print("-------------")

            elif operation == "-":
                answer = subtraction(number_1, number_2)

                print("-------------")
                print(f"Answer: {answer}")
                print("-------------")

            elif operation == "*":
                answer = multiplication(number_1, number_2)

                print("-------------")
                print(f"Answer: {answer}")
                print("-------------")

            elif operation == "/":
                answer = division(number_1, number_2)

                print("-------------")
                print(f"Answer: {answer}")
                print("-------------")

        else:
            print("🔴Enter valid Operation🔴")

        choice = input("Do you want another calculation? (Y/N): ").upper()
        if choice == "N":
            print("👋 Thanks for using the calculator!")
            break


# //-----------------\\

if __name__ == "__main__":
    main()
