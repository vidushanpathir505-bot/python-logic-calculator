import math

print("🧮 Welcome to Simple Calculator!")

# //-----------------\\

def addition(a,b):
    return a + b

# //-----------------\\

def subtraction(a,b):
    return a - b

# //-----------------\\

def multiplication(a,b):
    return a * b

# //-----------------\\

def division(a,b):
#Handle division by zero
    if b == 0:
        return "🟡Cannot divide by zero🟡"
    
    return a / b

# //-----------------\\

def power(a,b):
    return a ** b

# //-----------------\\

def sqrt(a):
#Handle negative number sqrt
    if a < 0:
        return '🟡Cannot take square root of negative number🟡'
            
    return math.sqrt(a)

# //-----------------\\

def get_valid_input():
#Getting valid input
    while True:
        try:
            number = float(input('Enter your number: '))
            return number
        except ValueError:
            print('🔴Enter Valid Number🔴')

# //-----------------\\ 

def show_answer(ans):
#print the answer
    print('-------------')
    print(f'Answer: {ans}')
    print('-------------')

# //-----------------\\ 

'''Dictionary of operation'''
operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}   

# //-----------------\\  

def main():

    while True:

        operation = input("choose the operator (+,-,*,/,**,sqrt): ")

        if operation == "sqrt":

            number = get_valid_input()
            
            answer = sqrt(number)

            show_answer(ans=answer)

        elif operation == "**":

            print('🟢Enter your Number🟢')
            number_1 = get_valid_input()

            print('🟢Enter your power🟢')
            number_2 = get_valid_input()

            answer = power(number_1,number_2)

            show_answer(ans=answer)
                    
        elif operation in ['+', '-', '*', '/']:

            number_1 = get_valid_input()
            number_2 = get_valid_input()

            answer = operations[operation](number_1, number_2)

            show_answer(ans=answer)

        else:
            print('🔴Enter valid Operation🔴')
            
        choice = input("Do you want another calculation? (Y/N): ").upper()
        if choice == "N":
            print("👋 Thanks for using the calculator!")
            break   

# //-----------------\\ 

if __name__ == '__main__':
    main()