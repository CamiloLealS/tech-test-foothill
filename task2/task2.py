# Task 2: Infinite Arithmetic| in Python

def Add(numbers):
    if numbers == "":
        return 0
    num_list = [0 if num.strip() == '' else int(num) for num in numbers.split(',')]
    return sum(num_list)

askAgain = True

while askAgain:
    userInput = input("Enter numbers separated by commas(type 'quit' to exit): ")
    if userInput.lower() == 'quit':
        askAgain = False
    else:
        result = Add(userInput)
        print(f"The sum is: {result}")
