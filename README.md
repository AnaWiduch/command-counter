# command-counter
a simple accounting bot that receives several commands as input and performs calculations. The bot has an internal counter, which initially equals 0, and it uses it for calculations.

zero – resets the number to 0
add <number> – adds the number to the current value
minus <number> – subtracts the number from the current value
mul <number> – multiplies the current value by the number
div <number> – divides the current value by the number, rounding down
result – displays the intermediate result
exit – terminates the program
The number is always an integer!

Input:

A list of commands that ends with the "exit" command.

Output:

All intermediate program outputs.


Sample Input 1:
add 5
mul 5
result
exit

Sample Output 1:
25
