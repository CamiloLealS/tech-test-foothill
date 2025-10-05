Tech Test Foothill Technology: F# Fundamentals
--------------------------------------------------------------------------------------------
The first task was simple, but I think I overcomplicated it, edge cases like extra comma('2,3,'), 
generate a last empty string in the array when is converted from the input string. I choosed 
treat it like an invalid input, but i could've managed it deleting the last empty string from 
the array and just summing the previous numbers.
--------------------------------------------------------------------------------------------
2nd task has better validation for extra comma and empty strings ('2,,5,2').
--------------------------------------------------------------------------------------------
In the 3rd task, after more researching and reading, i could implemented validations like TryParse
for value errors and found the way to use multiple delimiters to split a string.
Realized that previous tasks could be improved with some of these practices.
In python I'm using regex, cause I'm trying to give my best solution, but in F# I'm trying to solve it
creatively without it.
--------------------------------------------------------------------------------------------
In the 4rd task, had to manage the input to identify the delimiter in the first line and only iterate the rest of the lines.
---------------------------------------------------------------------------------------------
In the 5th task, there are some differences in my code between languages for this solution,
because the task ask for a return INT from the function Add, so I had to use another ways to
reach the expected result.
Now I created a function in the F# code to validate the inputs and separate the responsibilities. Like I have it in Python code.
---------------------------------------------------------------------------------------------
In the 7th task, I created another function for the responsability of find the delimiter trying to improve my code.
This time I used the function Replace to manage the string of the first line of input to obtain the delimiter.
---------------------------------------------------------------------------------------------
In the 8th task, like the example, the size of each delimiter is 1, so I can use an Array of chars(the delimiters) in the Split function, then sum the numbers.
I had to fix 7th task, because I realized that I made a mistake in Python Code about the pattern in regex for delimiters.
---------------------------------------------------------------------------------------------
In the last task, I had to change the way to split the delimiters in the first line.
---------------------------------------------------------------------------------------------
This technical challenge helped me understand some of the fundamentals of the f# language, to improve my problem solving and string management skills.
I'm thankful for the opportunity!
