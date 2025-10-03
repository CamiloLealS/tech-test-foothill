//Task 5: Custom Delimiters

//"open System" to avoid prefixing functions like Int32, String, etc
open System

let SafeInt (n: string): int =
    let s = n.Trim()
    if s = "" then
        0
    else
        //try to parse the number and add it to the sum or print an error message
        match Int32.TryParse(s) with
        | (true, v) ->
            //check for negative numbers and print an error message
            if v < 0 then
                printfn "Error: Negatives not allowed: %d" v
                -1
            else
                v
        | (false, _) ->
            printfn "Error: Invalid number: '%s'" s
            -1

//Define Add function to sum numbers in a string separated by custom delimiters or new lines
let Add (numbers: string) : int =
    //handle empty input
    if String.IsNullOrWhiteSpace(numbers) then 0
    else
        //split input to find custom delimiter in the first line
        let mutable toFindDelimiter : string array = numbers.Split([|'\n'|], StringSplitOptions.None)

        //get the custom delimiter from the first line 
        let delimiter: char = toFindDelimiter[0].[toFindDelimiter[0].Length - 1]

        //remove the first element from the list to only have the numbers to sum
        toFindDelimiter <- toFindDelimiter[1..]

        //Join the remaining elements back into a single string
        let stringifyNewList = String.Join("\n", toFindDelimiter)
        
        //split input by custom delimiter or new lines
        let num_list : string array = stringifyNewList.Split([|delimiter ; '\n'|], StringSplitOptions.None)
        
        //initialize sum
        let mutable sum = 0

        //iterate through each number in the list
        for num in num_list do
            let toSum = SafeInt num //get the integer value or -1 if error
            if toSum = -1 then
                sum <- -1 //set sum to -1 to indicate an error has occurred
            else if sum <> -1 then //only add to sum if no previous errors
                sum <- sum + toSum
        sum

let mutable running = true

printfn "Multi-line mode. Define the delimiter in the first line (e.g '//[delimiter]') and then input the numbers to sum up in the next lines separated by your custom delimiter."
printfn "Leave empty a new line to finish input, or 'quit' to exit."

while running do
    let mutable inputLines : string list = []
    let mutable finished = false

    //This way the user can input multiple lines of numbers, cause previously "Enter" avoid to input new lines
    while not finished && running do
        printf "> "
        let line: string = Console.ReadLine()

        match line.Trim().ToLower() with
        | "quit" ->
            printfn "Bye."
            running <- false
            finished <- true
        | "" -> 
            finished <- true
        | _ ->
            inputLines <- inputLines @ [line]

    if running then
        //Join all input lines into a single string with commas and new line separators
        let allInput = String.Join("\n", inputLines) 
        let result= Add allInput

        //-1 indicates an error has occurred, so we only print the result if no errors
        if result <> -1 then
            printfn "The sum is: %d" result
        printfn "----------------------------------------------"
