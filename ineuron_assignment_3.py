#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# 1. Why are functions advantageous to have in your programs?
Ans: 
Functions are advantageous to have in programs for several reasons:

Code Reusability: Functions allow you to define a block of code that can be reused multiple times throughout a program. Once a function is defined, you can call it whenever you need to perform a specific task, eliminating the need to duplicate the code. This promotes code reuse, reduces redundancy, and makes the code more modular and maintainable.

Modularity: Functions help break down complex programs into smaller, more manageable pieces. By dividing a program into smaller functions, each responsible for a specific task, you can achieve better organization and structure. This modular approach enhances readability, code organization, and makes it easier to understand and debug the program.

Abstraction: Functions also allow to abstract away the implementation details of a particular task. By encapsulating a set of instructions within a function, one can provide a high-level interface to other parts of the program, hiding the internal complexity. This promotes code simplification, improves code readability.

Code maintenance: Functions make it easier to update and maintain code. When there are separate functions for different tasks, modifying or fixing a particular functionality becomes more straightforward and localized. This reduces the risk of introducing errors and simplifies the debugging process. It also enables teams to work on different parts of a program simultaneously, enhancing development efficiency.

Code organization and readability: Functions promote code organization by logically separating different tasks or operations. By providing meaningful names to functions, we can enhance code readability and make the program's purpose and functionality more explicit. Well-organized and readable code is easier to understand, maintain, and debug.

Overall, functions enhance code reuse, modularity, abstraction, maintenance, and readability, making programs more efficient, manageable, and maintainable.
# 2. When does the code in a function run: when it's specified or when it's called?
Ans: 
The code in a function in Python runs when the function is called. Defining a function does not execute its code immediately; it simply defines the function's name, parameters (if any), and the block of code that will be executed when the function is called.

To execute the code within a function, you need to call the function by using its name followed by parentheses, optionally passing any required arguments. When the function is called, the program flow jumps to the function definition, executes the code within the function's block, and then returns to the point of the program where the function was called.


For example: 

def welcome(name):
    print("Hello, " + name + "!")

# Function defined, but code is not executed yet

greet("Gaurav")
# Function is called with the argument "Gaurav"
# Output: Hello, Gaurav!

greet("Sharma")
# Function is called again with the argument "Sharma"
# Output: Hello, Sharma!

In the example, the code within the greet function is executed only when the function is called, not when it is defined. The output is produced when the function is called with different names as arguments.
# 3. What statement creates a function?
Ans: 

In Python, the def statement is used to create a function. It is followed by the name of the function, parentheses, and a colon. Here is the syntax:

def function(parameters):
    # Code block
    # ...



def: It is the keyword used to indicate the start of a function definition.
function: This is the name given to the function, following Python's naming conventions. Choose a descriptive name that reflects the purpose or action performed by the function.
parameters: These are optional placeholders for data that can be passed into the function when it is called. Multiple parameters can be separated by commas, or you can have no parameters at all.

For example below is a user defined function that calculates the square of a number:


def square(x):
    result = x ** 2
    return result

# 4. What is the difference between a function and a function call?
The difference between a function and a function call lies in their respective roles and actions within a program:

Function: A function is a named block of reusable code that performs a specific task or action. It is defined using the def statement in Python. Functions can have parameters (optional) to accept input values, and they can return a result (optional) after executing the code block. Functions are defined once and can be called or invoked multiple times from different parts of a program.

Function Call: A function call is the actual execution or invocation of a function at a specific point in the program. When a function is called, the program flow transfers to the function's definition, executes the code within its block, and then returns to the point where the function was called. Function calls are made by using the function's name followed by parentheses, optionally passing any required arguments within the parentheses.

Here's an example to illustrate the difference between a function and a function call:

def welcome(name):
    print("Hello, " + name + "!")

# Function defined, but code is not executed yet

greet("Gaurav")
# Function is called with the argument "Gaurav"
# Output: Hello, Gaurav!


In the example, welcome is the function that is defined using the def statement. It takes a name parameter and prints a greeting message. The function call greet("Gaurav") invokes the greet function, passing the argument "Gaurav". This causes the function's code block to execute, printing the greeting message "Hello, Gaurav!".

Thus, a function is a defined block of reusable code, while a function call is the act of executing that code by invoking the function with appropriate arguments.
# 5. How many global scopes are there in a Python program? How many local scopes?
Ans: 

In Python, there is usually one global scope and multiple local scopes.

Global Scope: The global scope refers to the outermost level of a Python program. It is the top-level scope where variables and functions defined outside of any functions or classes are accessible. Variables defined in the global scope are accessible from anywhere within the program, including within functions and classes.

Local Scopes: Local scopes are created whenever a function or a class method is called. Each function call creates its own local scope, which is separate and independent from other local scopes. Variables defined within a function's code block or as function parameters belong to the local scope of that function. These variables are accessible only within that specific function's scope and are not visible outside of it. Similarly, methods within a class create their own local scopes.

Local scopes are temporary and are created and destroyed dynamically as functions or methods are called and return. Each time a function or method is called, a new local scope is created with its own set of variables. Local scopes can access variables from higher-level scopes, such as the global scope or enclosing function scopes (in the case of nested functions), but the reverse is not true. Variables defined within a local scope are not accessible outside of that specific scope.
# 6. What happens to variables in a local scope when the function call returns?
Ans: Local scopes are temporary and are created and destroyed dynamically as functions or methods are called and return. Each time a function or method is called, a new local scope is created with its own set of variables. Local scopes can access variables from higher-level scopes, such as the global scope or enclosing function scopes (in the case of nested functions), but the reverse is not true. Variables defined within a local scope are not accessible outside of that specific scope.
# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
Ans: 
The concept of a return value in programming refers to the value that a function provides back to the caller after it completes its execution. When a function is called and reaches a return statement, it immediately terminates the function and passes the specified value (if any) back to the caller. The return value can be used in various ways, such as assigning it to a variable, using it in an expression, or passing it as an argument to another function.

It is possible to have a return value in an expression. In Python, one can directly use the return value of a function within an expression or assign it to a variable for later use.

def multiply(x, y):
    return x * y

result = multiply(5, 3) + 2
print(result)  # Output: 17

In this example, the multiply function returns the product of two numbers x and y. The return value of multiply(5, 3) is then used in an expression where it is added to 2. The result, 17, is assigned to the variable result and subsequently printed.

# 8. If a function does not have a return statement, what is the return value of a call to that function?
Ans: 
If a function does not have a return statement, or if the return statement is omitted, the function will implicitly return the value None.

None is a special Python object that represents the absence of a value. It serves as a default return value when no explicit return statement is provided in a function. When a function without a return statement is called, it will execute its code and then automatically return None to the caller.

Example: 

def func_1():
    print('Hello')

result = func_1()
print(result)
#Output  
Hello
None
# 9. How do you make a function variable refer to the global variable?
Ans: 
To make a function variable refer to the global variable within a function, you can use the global keyword in Python. By using the global keyword, you indicate that a variable inside the function should refer to the global variable of the same name, rather than creating a new local variable.

# 10. What is the data type of None?
Ans: 
The data type of None is called NoneType. It is a built-in type in Python that has only one possible value, which is None. We can check the data type of None using the type() function, as mentioned below


result = None
print(type(result))  # Output: <class 'NoneType'>


The <class 'NoneType'> indicates that None belongs to the NoneType class. It is important to note that None is not the same as an empty string (''), an empty list ([]), or a value of zero (0). It is a distinct value representing the absence of a value.
# 11. What does the sentence import areallyourpetsnamederic do?
Ans: In Python, the import statement is used to bring functionality from external modules or packages into the code. However, "areallyourpetsnamederic" is not a recognized module name, so attempting to import it results in a ModuleNotFoundError as mentioned below.

---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[3], line 1
----> 1 import areallyourpetsnamederic

ModuleNotFoundError: No module named 'areallyourpetsnamederic'

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans: 
After importing the spam module, you can access the bacon() feature by referencing it using the dot notation. Here's an example:

import spam

spam.bacon()  # Calling the bacon() function from the spam module

In this code, spam is the name of the imported module, and bacon() is the function within the spam module needed to call. By prefixing the function name with the module name and a dot (spam.), we can access and use the bacon() feature provided by the spam module in the code.
# 13. What can you do to save a programme from crashing if it encounters an error?
Ans: 

To prevent a program from crashing when it encounters an error, we can use exception error handling to catch and handle the exceptions that occur. In Python, this can be done using the try-except statement. 

Here are a few things which can be done in the except block to prevent the program from crashing:

1. Print an error message or log the error for debugging purposes.
2. Perform alternative actions or provide fallback values.
3. Retry the operation that caused the exception.
4. Exit the program or perform cleanup tasks.

By handling exceptions, it can be ensured that the program continues to run even if errors occur. However, it's essential to handle exceptions appropriately. one needs to be specific to the types of exceptions to catch and consider the potential consequences of suppressing or bypassing errors.
# 14. What is the purpose of the try clause? What is the purpose of the except clause?
Ans: 

The try and except clauses are part of the try-except statement in Python, which is used for exception handling. The try clause is responsible for enclosing the code that might raise an exception. Its purpose is to identify the section of code where exceptions may occur.

The primary purpose of the try clause is to attempt the execution of the code within it. If an exception occurs during the execution of the code inside the try block, the program flow immediately jumps to the corresponding except clause.

On the other hand, the except clause is used to define the code that will handle the exception. It specifies the type of exception to catch and the actions to be taken when that particular exception is raised.

The purpose of the except clause is to provide a block of code that executes when a specific exception occurs within the try block.



try:
    (
    'code that may cause error'
    )
except ExceptionType:
    (
    'exception handling and the code to proceed accordingly'
    )
    

In this code, the potentially problematic code is placed inside the try block. If an exception of type ExceptionType or any of its subclasses is raised within the try block, the program will jump to the corresponding except block to handle the exception.
