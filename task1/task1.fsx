//Task 1: Simple Summation

//Define a function that sums up to two numbers given in a string input
let Add (numbers: string) : int =
    //Handle empty input and parse string to int for summation
    match numbers with
    | "" -> 0
    | _ ->
        //Split the input string separated by commas becoming in a string array
        let numbers = numbers.Split(separator = ',')

        //Check if there are more than 2 numbers, if so return -1 as an error code
        if numbers.Length > 2 then -1
        else
            //Initialize a mutable variable for the sum
            let mutable sum = 0
            //Iterate through the array, parsing each string to int and adding it to the sum
            for number in numbers do
                if number.Trim() = "" then 
                    sum <- sum + 0 //Handle case of empty string between commas or at the end (took it from task 2 resolution)
                else
                    let n = System.Int32.Parse(number)
                    sum <- sum + n
            //Return the final sum
            sum

//Initialize a variable to decide when to stop asking for input to the user
let mutable askAgain = true

while askAgain do
    printf "Enter 2 numbers separated by commas:(type 'quit' to exit) "
    let input = System.Console.ReadLine()

    //Check if user wants to quit or continue
    match input with
    | "quit" -> askAgain <- false
    | _ -> 
        //Call the Add function
        let result = Add input

        //Check for error code(More than 2 numbers or invalid input) and print the result
        if result = -1 then
            printfn "Error: More than 2 numbers or invalid input(extra comma) provided."
        else
            printfn "The sum is: %d" result
