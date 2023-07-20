#!/usr/bin/env python
# coding: utf-8

# # Assignment 6

# Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
Ans: 

Keywords in Python are reserved words that have a predefined meaning and cannot be used as identifiers (variable names, function names, etc.). These keywords are used to define the syntax and structure of the Python language.

Below is the code for printing all keywords.
# In[4]:


import keyword
print(keyword.kwlist)


# Q.2. What are the rules to create variables in python?

# Ans: 
# 
# In Python, variables are used to store values and provide a way to access and manipulate data. Here are the rules to create variables in Python:
# 
# 
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 
# The first character can be followed by letters, underscores, or digits (0-9).
# Variable names are case-sensitive, so myVariable and myvariable are considered different variables.
# 
# Reserved keywords cannot be used as as variable names. For example, if, while, for, etc., are reserved keywords and cannot be used as variable names.
# 
# Other than the reserved keywords, it is also important not to use the built-in functions as variable names as they may cause errors in the program.
# 
# The naming convention should follow best practices as python is case sensitive. Though not mandatory, it will be better to use
# lower case names for variables and user defined functions to avoid conflict and errors.
# 
# For example, variable_1, user_name, count_of_person etc.

# Q.3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
Ans: 

In Python, there are established standards and conventions for variable naming that help improve code readability and maintainability. The most widely followed convention is outlined in Python Enhancement Proposal 8 (PEP 8), which provides guidelines for writing Python code.

Variable names should be clear and describe the purpose or content of the variable.
 Single-character variable names (except for simple loop counters) could be avoided.
Instead, names that convey the meaning of the data being assigned should be used.
Lowercase letters with underscores (snake_case) should be used.

for example user_name, roll_num, age etc.

Variable names should be written in lowercase letters.
If a variable name consists of multiple words, separate them with underscores (_).
This convention improves readability and distinguishes variable names from class names.

A single leading underscore (_) indicates a weak "internal use" indicator.
It suggests that the variable is intended for internal use within a class or module.
It is a convention, not enforced by the Python interpreter.
Constants in uppercase letters:

If a variable represents a constant value that should not be modified, it should be assigned in uppercase letters.
Separate words with underscores (_) for readability.


# Q.4. What will happen if a keyword is used as a variable name?
Ans: 
    
If we try to use a keyword as a variable name, we will get a syntax error as the interpretor will try to use the keyword in its intended form and will not be able to assign it as a variable. For example in the below code, we try to assing the keyword while as a variable and as soon as we try to run it and error is thrown.

while = 1

Cell In[5], line 1
    while = 1
          ^
SyntaxError: invalid syntax
# Q.5. For what purpose def keyword is used?
Ans: 

The def keyword in Python is used to define a function. Functions are reusable blocks of code that perform specific tasks. They encapsulate a set of instructions and can be called multiple times throughout a program, allowing for modular and organized code structure.

Below is the syntax of a function definition in Python:

def function(parameters):
    
def: This keyword signals the start of a function definition.

function: This is the identifier or name given to the function. Choose a meaningful name that describes the purpose of the function.

parameters: These are optional inputs to the function. They are placeholders for values that can be passed to the function when it is called. Parameters are enclosed in parentheses and separated by commas.

Function body: This is the block of code that defines what the function does. It consists of one or more statements indented under the function definition line. It may include variable assignments, conditional statements, loops, and other Python code.

return statement (optional): A function can have a return statement to specify the value it should return when called. This statement is used to exit the function and return a value back to the caller.
# Q.6. What is the operation of this special character ‘\’?
Ans: 
The special character \ in Python is called the backslash or escape character. It serves several purposes and is used for different operations:

Escape sequences: The backslash is used to create escape sequences in strings. An escape sequence is a combination of the backslash and another character that represents a special character or a control sequence. Some commonly used escape sequences include:

\': Single quote
\": Double quote
\\: Backslash
\n: Newline
\t: Tab
\r: Carriage return
\b: Backspace
\f: Form feed
\ooo: Octal value (where ooo is a three-digit octal number)
\xhh: Hexadecimal value (where hh is a two-digit hexadecimal number)

These escape sequences are used to include special characters or control sequences within strings that would otherwise be difficult to represent directly.

Line continuation: The backslash is used as a line continuation character to split long lines of code into multiple lines for better readability. By placing a backslash at the end of a line, the text string can be printed in the line below.

string1 = "This is a very long string that requires \
               multiple lines for better readability."
               
In this example, the backslash at the end of the first line indicates that the string continues on the next line. The actual string does not contain the backslash or the line break.

Special characters: The backslash is used to include special characters within string literals. For example, to include a newline character within a string, you can use the escape sequence \n.


# Q.7. Give an example of the following conditions:
# 
# (i) Homogeneous list
# 
# (ii) Heterogeneous set
# 
# (iii) Homogeneous tuple
Ans: 
Below are the examples.

(i) Homogeneous list:
A homogeneous list in Python is a list where all the elements have the same data type. Below is an example of a homogeneous list of integers. The elements of the homogenous_list are integers.


homogenous_list = [1, 2, 3, 4, 5]


(ii) Heterogeneous set:
A heterogeneous set in Python is a set where the elements can have different data types. Below is an example.
The below set heterogeneous_set contains elements of different data types, including an integer, a string, a floating-point number, and a boolean.


heterogeneous_set = {1, "hello", 3.14, True}


(iii) Homogeneous tuple:
A homogeneous tuple in Python is a tuple where all the elements have the same data type. Below is an example of a homogeneous tuple of strings. All the elements of the homogenous_tuple are strings

homogenous_tuple = ("apple", "banana", "orange")


# Q.8. Explain the mutable and immutable data types with proper explanation & examples
Ans: 

The distinction between mutable and immutable data types impacts how data is manipulated, passed between functions, and stored in data structures. Mutable objects can be modified in-place, while immutable objects require the creation of new objects when changes are needed.

Mutable Data Types:

Mutable data types are those whose values can be modified after they are created.
When you modify a mutable object, you are actually changing its contents in-place without creating a new object.
Examples of mutable data types in Python include lists, sets, and dictionaries.

Immutable Data Types:

Immutable data types are those whose values cannot be changed once they are created.
When you "modify" an immutable object, you are actually creating a new object with the modified value.
Examples of immutable data types in Python include integers, floats, booleans, strings, and tuples.Q.9. Write a code to create the given structure using only for loop.

      *
     ***
    *****
   *******
  *********
# In[6]:


#Ans: Below is the code

rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

Q.10. Write a code to create the given structure using while loop.
 |||||||||
  |||||||
   |||||
    |||
     |
# In[8]:


#Ans: Below is the code

rows = 5
i = 0

while i < rows:
    # Print spaces before the bars
    j = 0
    while j < i:
        print(" ", end="")
        j += 1

    # Print the bars
    k = 0
    while k < 2 * (rows - i) - 1:
        print("|", end="")
        k += 1

    print()  # Move to the next line
    i += 1


# In[ ]:




