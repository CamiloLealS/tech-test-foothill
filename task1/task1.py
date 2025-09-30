# Task 1: Simple summation | in Python

def Add(numbers):
    if numbers == "":
        return 0
    num_list = [int(num) for num in numbers.split(',')]
    if len(num_list) > 2:
        return -1
    return sum(num_list)

askAgain = True

while askAgain:
    userInput = input("Enter numbers separated by commas:(type 'quit' to exit) ")
    if userInput.lower() == 'quit':
        askAgain = False
    else:
        result = Add(userInput)
        if result == -1:
            print("Error: More than 2 numbers or invalid input(extra comma) provided.")
        else:
            print(f"The sum is: {result}")
