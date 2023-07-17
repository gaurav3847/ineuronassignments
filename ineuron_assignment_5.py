#!/usr/bin/env python
# coding: utf-8

# # Assignment 5

# 1. What does an empty dictionary's code look like?
Ans: 

An empty dictionary code looks like two closing braces {} which indicated that there are no keys or values inside the disctionary. Alternatively it can also be denoted as dict().
# 2. What is the value of a dictionary value with the key 'foo' and the value 42?

# Ans: 
# Below is the code. We can define the dictionary whith key "foo" and its corresponding value as 42 as mentioned below.
# if we print the key from the dictionary dict1. it will print its value which is 42. Hence the value is 42
#     
# dict1 = {'foo': 42}
# print(dict1['foo'])
# #output = 42

# 3. What is the most significant distinction between a dictionary and a list?
Ans: The most significant distinction between a dictionary and a list is the organizational structure and the way data is accessed. Lists are ordered collections accessed by indices, while dictionaries are unordered collections accessed by keys.

Organization:

Lists are ordered collections of items that can be accessed and manipulated using indices. The order of elements in a list is based on their position in the list, starting from index 0.
Dictionaries, on the other hand, are unordered collections of key-value pairs. Each value is associated with a unique key, which allows for efficient retrieval of values based on their corresponding keys. The order of items in a dictionary is not guaranteed.

Accessing Data:

Lists are accessed and modified by using indices. Elements in a list can be accessed, added, removed, or modified using index-based operations.
Dictionaries, on the other hand, are accessed and modified using keys. Values in a dictionary are accessed, added, removed, or modified using key-based operations.
Data Structure:
Lists are typically used to store a collection of similar or related items. The elements within a list can be of different data types.

Dictionaries are commonly used to store key-value pairs, where each key is unique and associated with a specific value. The values within a dictionary can be of different data types, but the keys must be immutable (such as strings, numbers, or tuples).
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Ans:

Below is the code. If the variable spam is declared as a dictionary with key - 'bar' and value 100, the variable will store it as follows: 

spam = {'bar' : 100}

and if we try to access spam['foo'] we will get a KeyError as the key - 'foo' is not present in the disctionary spam. 

spam['foo']

KeyError                                  Traceback (most recent call last)
Cell In[1], line 2
      1 spam = {'bar' : 100}
----> 2 spam['foo']

KeyError: 'foo'

To access key - 'foo, it needs to be declared in the dictionary with the corresponding value as show below.

spam = {'bar' : 100 , 'foo' : 'value'}

spam['foo']

#Output = 'value'
# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Ans: 

The expressions 'cat' in spam and 'cat' in spam.keys() have slightly different meanings when applied to a dictionary stored in the variable spam.

'cat' in spam:
This expression checks if the key 'cat' exists in the dictionary spam. It returns a Boolean value (True or False) indicating whether the key is present or not. It checks for the presence of the key directly within the dictionary.
For example:

spam = {'cat': 1, 'dog': 2}
print('cat' in spam)  
#Output  = True

In the code above, 'cat' in spam returns True because the key 'cat' is present in the spam dictionary. 

'cat' in spam.keys():

This expression checks if the key 'cat' exists in the list of keys obtained from the spam dictionary using the keys() method. It returns a Boolean value indicating whether the key is present among the keys of the dictionary.
For example:

print('cat' in spam.keys())  
#Output = True

In the code above, 'cat' in spam.keys() also returns True because the key 'cat' is present among the keys obtained from the spam dictionary using keys(). 

Both expressions ultimately check if the key is present in the dictionary, but the second expression explicitly uses the keys() method to obtain the keys before performing the check.
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
Ans: 

Taking the same example as above. 'cat' in spam checks if 'cat' is a key in the spam dictionary, while 'cat' in spam.values() checks if 'cat' is a value in the spam dictionary.

'cat' in spam:
This expression checks if the key 'cat' exists in the dictionary spam. It returns a Boolean value (True or False) indicating whether the key is present or not. It checks for the presence of the key directly within the dictionary.
For example:

spam = {'cat': 1, 'dog': 2}
print('cat' in spam)  

#Output = True

In the code above, 'cat' in spam returns True because the key 'cat' is present in the spam dictionary. 

Whereas

'cat' in spam.values():
This expression checks if the value 'cat' exists in the dictionary spam among the values stored in the dictionary. It returns a Boolean value indicating whether the value is present or not.

print(1 in spam.values())  
Output = True
# 7. What is a shortcut for the following code?
# 
# if 'color' not in spam:
# 
# spam['color'] = 'black'
# 
Ans: 
The shortcut for the given code can be achieved using the dict.setdefault() method. The setdefault() method allows you to specify a default value for a key in a dictionary if the key is not already present. Here's the equivalent shortcut:


spam.setdefault('color', 'black')
The setdefault() method checks if the key 'color' exists in the spam dictionary. If it does, the method returns the corresponding value. If the key doesn't exist, the method sets the key with the specified default value 'black' and returns that value.

In this case, if 'color' is not in spam, the code will set 'color' to 'black'. If 'color' is already present, it will retain its existing value.
# 8. How do you "pretty print" dictionary values using which module and function?
Ans: 

To "pretty print" dictionary values in a well-formatted and readable manner, you can make use of the pprint module in Python and its pprint() function.

For example:

import pprint

dict1 = {'name': 'Gaurav', 'age': 30, 'roll': 18}
pprint.pprint(dict1)

#Output = 

{'age': 30,
 'name': 'Gaurav',
 'roll': 18}
 
 
In the code above, we import the pprint module. Then, we define a dictionary my_dict with some key-value pairs. By calling pprint.pprint(my_dict), the dictionary is printed in a more readable format. The key-value pairs are displayed with indentation, each on a separate line.

