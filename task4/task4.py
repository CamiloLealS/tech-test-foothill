# Task 4: Custom Delimiters | in Python
import re

def safe_int(s):
    s = s.strip()
    if s == "":
        return 0
    try:
        return int(s)
    except ValueError:
        print(f"This is not a valid number: {s}")
        return 0

def Add(numbers):

    delimiter = re.split(r'\n', numbers)[0][-1]
    num_list = "\n".join(re.split(r'\n', numbers)[1:])
    pattern = rf'[{delimiter}\n]+'

    if numbers == "":
        return 0

    return sum(safe_int(num) for num in re.split(pattern, num_list))

askAgain = True

print("Multi-line mode. You can enter numbers separated by commas or new lines.")
print("Leave empty a new line to finish input, or 'quit' to exit.")

while askAgain:
    inputLines = []

    while True:
        userInput = input("> ")

        if userInput.lower() == 'quit':
            inputLines = ['quit']
            break
        if userInput == "":
            break
        inputLines.append(userInput)

    allInput = "\n".join(inputLines)

    if allInput.lower() == 'quit':
        askAgain = False
    else:
        result = Add(allInput)

        print(f"The sum is: {result}")
        print("-------------------------------------------")
