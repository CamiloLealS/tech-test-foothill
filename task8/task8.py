# Task 8: Multiple Delimiters | in Python
import re

def safe_int(s, negatives, invalids, giants):
    s = s.strip()
    if s == "":
        return 0
    try:
        if int(s) < 0:
            negatives.append(s)
        if int(s) > 1000:
            giants.append(s)
            return 0
        return int(s)
    except ValueError:
        invalids.append(s)   
        return 0
    
def FindDelimiter(input):
    # Split input to find custom delimiter in the first line
    delimiters = re.split(r'\n', input)[0].replace("//", "").replace("[", "").replace("]", "").split()
    num_list = "\n".join(re.split(r'\n', input)[1:])

    # Escape delimiters for regex
    escaped = [re.escape(d) for d in delimiters]

    # Create regex pattern to split by any of the delimiters or new lines
    pattern = rf"(?:{'|'.join(escaped)}|\n)+"

    return pattern, num_list


def Add(numbers):
    pattern, num_list = FindDelimiter(numbers)

    if numbers == "":
        return 0

    negatives = []
    invalids = []
    giants = []

    return sum(safe_int(num, negatives, invalids, giants) for num in re.split(pattern, num_list)), negatives, invalids, giants


askAgain = True

print("Multi-line mode. You can enter numbers with maximum 3 digits separated by commas or new lines.")
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
        result, negatives, invalids, giants= Add(allInput)

        if negatives:
            print(f"Negatives not allowed: {', '.join(negatives)}")

        if invalids:
            print(f"These are not valid numbers: {', '.join(invalids)}")

        if not negatives and not invalids:
            if giants:
                print(f"These numbers are too large and will be ignored: {', '.join(giants)}")
            print(f"The sum is: {result}")

        print("-------------------------------------------")
