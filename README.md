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
--------------------------------------------------------------------------------------------
In the 4rd task, had to manage the input to identify the delimiter in the first line and only iterate the rest of the lines.
---------------------------------------------------------------------------------------------