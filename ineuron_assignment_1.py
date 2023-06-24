#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# * 
# 'hello'
# -87.8
# - 
# / 
# +	
# 6 
Ans: In the above statement 'hello',-87.8, 6 are values  and  * , - , /, + are expressions
# 2. What is the difference between string and variable?
Ans: A string is a set of apha numeric values, which is usually stored in quotes (""). This is used as text form of data.
For example, in the code print("Hello World") the text Hello World is a string.

A variable in python is a character like x,y or a name like name_1, phone_1 etc which are used to declare or store data types
in the memory. The data could be a string, integer or float.

For example, in below code x, y and name_1 are variables.
x=1
y=2
name_1 = Gaurav
print (x,y,name_1)

# 3.Describe three different data types.
Ans: The three different data types are String, Integer and Float
    
String(): A string data type consists of textual data, which could be alpha-nuemric in nature and needs to be stored in quotes.
For example, in the following code: name = ('Gaurav'), last_name = ('@Sharma123'), both Gaurav and @Sharma123 are stored as 
strings since they are in quotes. Strings are used to store/declare names or long aplhanumeric texts as inputs 
or declared valiables

Integer(): An integer data type is only numeric integers or whole numbers i.e. not decimal or fractions. They do not need to be 
declared/stored in quotes.
For example: in the following code: x=10, y=2212, both 10 and 2212 are integers.

Float(): A float data type is the one which is used to declare/store decimal values but is not limited to that. Float can aslo be used to store/declare integers as well. A integer declared as float will show a decimal point at the end.
For example: x= float(1.23), y = 2.35, here bothe 1.23 and 2.35 are stored as float data type.

By default python stores the data types as string or numeric as declared, however, it would be a good practice to declare data type as intended for the code by using x= int(), y = float().
# 4. What is an expression made up of? What do all expressions do?
Ans: An expression is made up of values and operators such as *, /, +, - ,%, //, **, >>, << among others.
The purpose of an expression is to evaluate and provide an out put based on the input values and the operators used.

for example, 
x=5
y=2
add = x + y
sub = x - y
div = x / y
mul = x * y
exp = x**y
per = x % y
spe = x // y


print (add)
print (sub)
print (div)
print (mul)
print (exp)
print (per)
print (spe)

In the above code all the lines of code above the print statement are an expression and are supposed 
solve for eg x+y = 7 based on the input provided.
# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans: Like the statement provided in the spam = 10 the variable spam is being assigned the value 10. 
This is a statement in in python as it is providing an instruction to perform a task which in this 
case is to assign a value. Similarly, the print () statement will intruct the kernel to print the output 
based on the assigment and any expressions if coded.

The basic difference between a statement and an expression is that a statement can contain a expression but an 
expression may not have a statement. Also, an expression will execute the given operation based on the operator
however, to see that output a statement would be required such as print()

Basically, every line of code can be considered a statement which can inturn have expression or combination of
functions and expressions which decide the logical flow of the python code

for example, 
x=5
y=2
add = x + y
sub = x - y

print (add)
print (sub)

Here, x=5, y=2, add = x + y, sub = x - y, print (add), print (sub) all these lines of code are statements
and x+y , x-y are expressions.
# 6. After running the following code, what does the variable bacon contain?
# 
# bacon = 22
# bacon + 1
# 
Ans: 

bacon = 22
bacon + 1

In the given code we are first assigning variable bacon a value of 22.
In the next line the statement states to do an increment of 1 using the expression bacon + 1.
Hence the variable bacon would contain a value of 23.
# 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 
Ans:

'spam' + 'spamspam'
'spam' * 3

Both the expressions will give the same output 'spamspamspam'
# 8. Why is eggs a valid variable name while 100 is invalid?
Ans: Variable names can contain letters (both uppercase and lowercase), digits, and underscores (_). 
They must start with a letter or an underscore. However, digits are not allowed as the first character of a variable name.

It is a convention in Python to use lowercase letters for variable names. While uppercase letters are allowed, 
it is recommended to use them for constants or special cases. 
For example, eggs is a valid variable name, whereas Eggs or EGGS are also valid but not following the conventional naming style.

Thus, 

eggs is a valid variable name because it starts with a lowercase letter and contains only letters. 
It adheres to the naming conventions.

100 is not a valid variable name because it starts with a digit, which is not allowed as the first character. 
Variable names must begin with a letter or an underscore.

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
We can use the following three functions to convert a value to an integer, floating-point number, or string version:

int(): This function is used to convert a value to an integer. It takes a parameter and attempts to convert it into an integer 
type. If the value can be successfully converted, the integer representation is returned. 

for ex: 
value = "42"
integer_value = int(value)
print(integer_value)  # Output: 42

float(): This function is used to convert a value to a floating-point number. It takes a parameter and tries to convert 
it into a floating-point number type. 

for ex
value = "3.14"

float_value = float(value)
print(float_value)  # Output: 3.14
str(): This function is used to convert a value to a string. It takes a parameter and returns a string representation 
of the value. This function can convert various types, including numbers, booleans, and objects, into a string.

for ex
value = 42
string_value = str(value)
print(string_value)  # Output: "42"

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# 
Ans: 'I have eaten ' + 99 + ' burritos.'

In the above expression, the first part of the expression 'I have eaten ' and the last part of the expression ' burritos'
are string values whereas the middle part of the expression 99 is an integer. The python operator + can be used to concat
two strings or two numbers. It is not possible in python to contact a string and a integer using + . Hence in order to fix the 
expression we need to convert 99 in to a string, which can be done using below to methods.

1. 'I have eaten ' + '99' + ' burritos.'
2. 'I have eaten ' + str(99) + ' burritos.'