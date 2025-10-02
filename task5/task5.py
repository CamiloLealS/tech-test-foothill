# Task 5: Negative Rebellion | in Python
import re

def safe_int(s, negatives, invalids):
    s = s.strip()
    if s == "":
        return 0
    try:
        if int(s) < 0:
            negatives.append(s)
        return int(s)
    except ValueError:
        invalids.append(s)   
        return 0

def Add(numbers):

    delimiter = re.split(r'\n', numbers)[0][-1]
    num_list = "\n".join(re.split(r'\n', numbers)[1:])
    pattern = rf'[{delimiter}\n]+'

    if numbers == "":
        return 0

    negatives = []
    invalids = []
    return sum(safe_int(num, negatives, invalids) for num in re.split(pattern, num_list)), negatives, invalids

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
        result, negatives, invalids = Add(allInput)

        if negatives:
            print(f"Negatives not allowed: {', '.join(negatives)}")

        if invalids:
            print(f"These are not valid numbers: {', '.join(invalids)}")

        if not negatives and not invalids:
            print(f"The sum is: {result}")

        print("-------------------------------------------")
