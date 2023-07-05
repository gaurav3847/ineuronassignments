#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# 1.What are the two values of the Boolean data type? How do you write them?
Ans: In Python, the two values of the Boolean data type are "True" and "False". These values are commonly used in Python for logical operations, conditional statements, and boolean expressions to control the flow of programs and make decisions based on specific conditions.

To write these Boolean values in Python, we would use the following:

True
False

It is important to note that the boolead data type are to be written with the first alphabet as capital as these are case seisitive in python.
# 2. What are the three different types of Boolean operators?
Ans: The three different types of Boolean operators are:

AND Operator: It returns "True" if both operands are true; otherwise, it returns "False".In Python, it is represented by the keyword "and".

OR Operator: It returns "True" if at least one of the operands is true; if both operands are false, it returns "False". It is represented by the keyword "or".

NOT Operator: It is a unary operator that returns the opposite of the operand's logical value. If the operand is "True", the NOT operator returns "False", and vice versa. It is represented by the keyword "not".

These Boolean operators are commonly used to combine or manipulate Boolean values in logical expressions and conditions.
# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
Ans: Below are the truth tables for each Boolean operator in Python:

AND Operator (and):

Operand 1 	Operand 2   Output
 FALSE	      FALSE	    FALSE
 FALSE	      TRUE	    FALSE
 TRUE	      TRUE	    FALSE
 TRUE	      TRUE	    TRUE


OR Operator (or):

Operand 1   Operand 2   Result  
  FALSE       FALSE     FALSE   
  FALSE       TRUE      TRUE    
  TRUE        FALSE     TRUE    
  TRUE        TRUE      TRUE    

NOT Operator (not):

  Operand   Result   
   FALSE    TRUE    
   TRUE     FALSE   

These truth tables illustrate the result of applying each Boolean operator to all possible combinations of Boolean values (True and False) in Python.
# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
Ans: Below are the values of the given expressions.

1. (5 > 4) and (3 == 5) ------>> FALSE

2. not (5 > 4) ------>> FALSE

3. (5 > 4) or (3 == 5)  ------>> TRUE

4. not ((5 > 4) or (3 == 5)) ------->> FALSE

5. (True and True) and (True == False) ------->> FALSE

6. (not False) or (not True) ------>> TRUE

7. 
# 5. What are the six comparison operators?
Ans: 

In Python, the six comparison operators are:

1. Equal to (==): Compares if two values are equal and returns True if they are, False otherwise.

2. Not equal to (!=): Checks if two values are not equal and returns True if they are not, False otherwise.

3. Greater than (>): Determines if the value on the left is greater than the value on the right and returns True if it is, False otherwise.

4. Less than (<): Determines if the value on the left is less than the value on the right and returns True if it is, False otherwise.

5. Greater than or equal to (>=): Checks if the value on the left is greater than or equal to the value on the right and returns True if it is, False otherwise.

6. Less than or equal to (<=): Checks if the value on the left is less than or equal to the value on the right and returns True if it is, False otherwise.

These operators are used to compare values and return boolean results based on the comparison.
# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
.Ans: 
The equal to operator (==) and the assignment operator (=) serve different purposes in Python.

The basic difference between the equal to operator (==) and the assignment operator (=), is that the equal to operator is used in comparisons, while the assignment operator is used to assign values to variables.

Equal to operator (==): The equal to operator is used for comparison. It checks whether the values on both sides of the operator are equal. It returns True if the values are equal and False otherwise. It is used in conditions and expressions to compare values.

Example:

x = 5
y = 10

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
    
In the above example, the == operator compares the values of x and y to determine if they are equal.

Assignment operator (=): The assignment operator is used to assign a value to a variable. It assigns the value on the right side of the operator to the variable on the left side. It does not perform a comparison, but rather updates the variable with a new value.

Example:

x = 5
y = x

print("The value of x is:", x)
print("The value of y is:", y)

In the above example, the = operator assigns the value of x to y, making y equal to 5.
# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 
Ans: 
The code has three blocks which are explained below.

spam = 0

if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
    
The three identified blocks in this code are:

Block 1:

if spam == 10:
    print('eggs')
    
This block consists of the if statement, which checks if the value of spam is equal to 10. If the condition is true, it executes the indented code, which is print('eggs').

Block 2:

if spam > 5:
    print('bacon')
    
This block also starts with an if statement, checking if the value of spam is greater than 5. If the condition is true, it executes the indented code, which is print('bacon').

Block 3:

else:
    print('ham')
This block is associated with the else statement, which is part of the previous if statement. If the condition in the previous if statement (Block 2) is false, this block is executed and print('ham') is executed.

The remaining print('spam') statements are not part of any block. They are executed sequentially after the previous blocks.
# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
Ans 

Below is  the code.

spam = 1 #or any assigned value

if spam == 1:
    print('Hello')
    
elif spam == 2:
    print('Howdy')
    
else:
    print('Greetings!')

# 9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans: 

If a program is stuck in an endless loop and you want to interrupt its execution, you can press the following keys depending on the OS.

Windows/Linux: Ctrl + C
macOS: Command + C

Pressing these key combinations sends an interrupt signal to the running program, causing it to terminate and break out of the loop. This can be used if a program is taking longer than expected to execute or is stuck in an infinite loop.
# 10. How can you tell the difference between break and continue?
Ans: 

In Python, break and continue are two different control flow statements used in loops (such as for and while) to alter the flow of execution.

While break terminates the loop entirely,continue skips the remaining code within the loop for the current iteration and moves to the next iteration.These statements serve different purposes and can be used to control the flow of execution within loops based on specific conditions or requirements.

break statement: The break statement is used to terminate the loop prematurely. When encountered within a loop, break immediately exits the loop, and the program continues with the next statement after the loop. It completely breaks out of the loop's execution.

Example:

for i in range(1, 6):
    if i == 3:
        break
    print(i)

Output:
1
2

In the above example, when i becomes 3, the break statement is executed, causing the loop to terminate immediately.

continue statement: The continue statement is used to skip the remaining code within a loop for the current iteration and move to the next iteration. When encountered, it stops the current iteration and proceeds with the next iteration of the loop.

Example:

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5

In the above example, when i becomes 3, the continue statement is executed. This skips the print(i) statement for that iteration and moves on to the next iteration.
# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
In a for loop, range(10), range(0, 10), and range(0, 10, 1) produce the same result and iterate over the numbers from 0 to 9. The three forms of range() have slightly different syntax, but they function the same in this scenario.

range(10): This form specifies the stop value of the range, which is 10 in this case. By default, the start value is 0, and the step value is 1. The resulting range will include numbers from 0 to 9 (10 is excluded).

Example:

for i in range(10):
    print(i)
Output:


0
1
2
3
4
5
6
7
8
9

range(0, 10): This form specifies both the start and stop values of the range. The range will include numbers starting from the start value (0) and ending at the stop value (10 is excluded), with a default step value of 1.

Example:

for i in range(0, 10):
    print(i)

Output:


0
1
2
3
4
5
6
7
8
9

range(0, 10, 1): This form specifies the start, stop, and step values explicitly. The range will include numbers starting from the start value (0) and ending at the stop value (10 is excluded), incrementing by the step value (1 in this case).

Example:

for i in range(0, 10, 1):
    print(i)

Output:


0
1
2
3
4
5
6
7
8
9

All three forms (range(10), range(0, 10), and range(0, 10, 1)) will produce the same sequence of numbers from 0 to 9. They differ only in syntax but result in the same iteration behavior within a for loop.
# 12. Write a short program that prints the numbers 1 to 10 using a for loop. 
# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Ans: 

Below are the two programs to print the given output.

1. With for loop:
    
for i in range (1,11):
    print(i)

2. With while loop:
    
i = 1
while i < 11:
    print(i)
    i+=1
# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Ans: 
After importing the module spam, we can call the function bacon() using a dot to reference the function within the module.
Below is an example.

import spam

spam.bacon()

In the code above, spam is the name of the imported module, and bacon() is the function within that module. 
By prefixing the function name with the module name and a dot (spam.bacon()), you can access and call the bacon() function.