#!/usr/bin/env python
# coding: utf-8

# # Assignment 4

# 1. What exactly is []?
In Python, the square brackets [ ] are primarily used to define lists and access the items in the list. List is a type of data structure in Python. Lists are ordered collections of items enclosed in square brackets, with each item separated by a comma.

For example:

list1 = [1, 2, 3, 4, 5]

In this example, list1 is a list containing the numbers 1, 2, 3, 4, and 5. The square brackets [ ] are used to denote the boundaries of the list
# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans: 

Please find below the code. Here spam is the name of the list and [2] is the third position in the list where we are assigning the value 'hello'
    
spam = [2,4,6,8,10]

spam[2] = 'hello'

print(spam)
# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 
# 3. What is the value of spam[int(int('3' * 2) / 11)]?
Ans: 

Please find below the code. Here the function int(int('3'*2)/11) gives out put as 33/11 = 3. so Spam[3] would return the 4th valiue in the list which is d.

spam = ['a', 'b', 'c', 'd']

spam[int(int('3'*2)/11)]

#Ouput = 'd'
# 4. What is the value of spam[-1]?
Ans: 
Please find below the code. Here -1 indcates the postion of the list from the end. Thus, the code will return the last value in the list which is d.

spam = ['a', 'b', 'c', 'd']

print (spam[-1])

#output = 'd'
# 5. What is the value of spam[:2]?
Ans: 
Please find below the code. Here the argument (spam[:2]) indicated the staring and the end point we want to return from te list. By leaving the starting position empty, the code would assume the first value in the list which is as position 0. Thus, the code will return first two items in the list which are 'a' and 'b'. 

spam = ['a', 'b', 'c', 'd']

print (spam[:2])

#output = ['a', 'b']
# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 
# 6. What is the value of bacon.index('cat')?
Ans: 

Please find below the code. Here the the code bacon.index method finds the first occurence of an item in a list. 
Thus, it returns the first occurence of the item 'cat' which is on the 1st postion in the list.
    
bacon = [3.14, 'cat', 11, 'cat', True] 

bacon.index('cat')

#Output = 1
# 7. How does bacon.append(99) change the look of the list value in bacon?
Ans: 
    
Below is the code. The append method appends the list the input value. That means the input value provided will be added to the list at the last postion. Thus, the list gets updated with 99 as the last item in the appended list.
    
bacon.append(99)

print(bacon)

#Output [3.14, 'cat', 11, 'cat', True, 99]
# 8. How does bacon.remove('cat') change the look of the list in bacon?
Ans: 
    
Below is the code. the remove method will remove an item in the list. In case, there a mulitple items with the same value in the list, it will remove the first occurence of the item as we can see in the below case the item 'cat' from the 1st position in the list has been removed.
    
bacon.remove('cat')

print(bacon)

#Output [3.14, 11, 'cat', True, 99]
# 9. What are the list concatenation and list replication operators?
Ans: 

In Python, the list concatenation operator is the plus sign (+), and the list replication operator is the asterisk (*). 

List Concatenation Operator (+):
The plus operator (+) is used to concatenate two or more lists, creating a new list that contains all the elements from the concatenated lists.

For example, here list1 and list2 are concatenated using the plus operator, resulting in a new list concat_list that contains all the items from both lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concat_list = list1 + list2
print(concat_list)

#Output = [1, 2, 3, 4, 5, 6]

List Replication Operator (*):

The asterisk operator (*) is used to replicate or repeat a list a specified number of times. It creates a new list by repeating the elements of the original list. 

For example, list1 is replicated 2 times using the * operator, resulting in a new list replicated_list that contains the elements of list1 repeated three times.

list1 = [1, 2, 3]
replicated_list = list1 * 2
print(replicated_list)
#Output = [1, 2, 3, 1, 2, 3]
 
# 10. What is difference between the list methods append() and insert()?
Ans: 

The append() and insert() methods are both used to add elements to a list in Python, but they differ in how they add the elements. Here's an explanation of each method:

append() method:
The append() method is used to add an element to the end of a list. It takes a single argument, which is the element to be added. The element is appended (added) to the end of the list, increasing its length by one. Here's an example:

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#Output = [1, 2, 3, 4]

insert() method:
The insert() method is used to add an element at a specific index position within a list. It takes two arguments: the index position where the element should be inserted and the element itself. The other elements in the list are shifted right to add the new element. 

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)

#Output = [1, 4, 2, 3]

# 11. What are the two methods for removing items from a list?
Ans: The two commonly used methods to remove items from a list are remove() and pop()

remove() method:
The remove() method is used to remove the first occurrence of a specific value from a list. It takes an element as an argument and removes it if it exists in the list. If the element is not found, it raises a ValueError. 

For example: 

list1 = [1, 2, 3, 4]
list1.remove(2)
print(list1)
#Output = [1, 3, 4]

pop() method:
The pop() method is used to remove an item from a list at a specified index. It takes an optional index as an argument. If no index is provided, it removes and returns the last item in the list. If an index is specified, it removes and returns the item at that index. The remaining elements in the list are shifted to fill the gap. 

For example:

list1 = [1, 2, 3, 4]
list1.pop(2)
print(list1)
#Output = [1, 2, 4]

# 12. Describe how list values and string values are identical.
Ans: Below are the similarities and differnces

Sequence Type: Both lists and strings are considered sequence types in Python. This means that they can be indexed and sliced to access individual elements or subsequences.

Indexing: Both lists and strings support indexing, allowing you to access individual elements by their position in the sequence. For example, my_list[0] would retrieve the first element of a list, and my_string[2] would retrieve the third character of a string.

Slicing: Both lists and strings support slicing, which enables you to extract subsequences by specifying start and end indices. For example, my_list[1:4] would retrieve a sublist containing elements at indices 1, 2, and 3, while my_string[2:5] would retrieve a substring consisting of characters at indices 2, 3, and 4.

Iteration: Both lists and strings can be iterated over using loops, allowing you to access each element or character sequentially.

Yet,  there are a few differences which separates them as mentioned below.

Mutability: Lists are mutable, meaning you can change their individual elements, add new elements, or remove existing elements. In contrast, strings are immutable, and their individual characters cannot be modified once the string is created.

Content: Lists can store a collection of different data types, including numbers, strings, and other objects. On the other hand, strings are specifically designed to store sequences of characters.

Methods: Lists and strings have different sets of built-in methods. Lists have methods like append(), pop(), and sort() that allow manipulation and modification of the list's contents. Strings have methods like split(), upper(), and replace() that are useful for string manipulation and transformation.
# 13. What's the difference between tuples and lists?
Ans: 

In Python, tuples and lists are both sequence data types, but they have several key differences:

Mutability: Tuples are immutable, meaning their elements cannot be modified after creation. In contrast, lists are mutable, allowing for the modification, addition, or removal of elements.

Syntax: Tuples are defined using parentheses ( ) or without any delimiters, whereas lists are defined using square brackets [ ].

Element Types: Tuples can store elements of different data types, such as integers, strings, and floats, within a single tuple. Lists, similar to tuples, can also store elements of different data types, but they are often used to contain homogeneous elements.

Usage: Tuples are typically used to represent collections of related, but different, items, where immutability is desired. For example, coordinates (x, y) or dates (year, month, day) can be represented using tuples. Lists, on the other hand, are commonly used when the order and the ability to modify elements are important, such as for maintaining a collection of items or performing operations like sorting or appending.

Performance: Tuples are generally more memory-efficient and faster to process than lists because of their immutability. Lists require additional memory allocation and copying when modified, whereas tuples do not.

Available Methods: Tuples have a limited set of built-in methods, including count() and index(), due to their immutability. Lists, being mutable, have a broader range of methods, such as append(), insert(), pop(), sort(), and more, that allow for dynamic modifications.
# 14. How do you type a tuple value that only contains the integer 42?
Ans: 

To create a tuple that contains only the integer 42,the following syntax can be used:

my_tuple = (42,)

In Python, when creating a tuple with a single element, it is necessary to include a trailing comma after the element. This distinguishes it from the use of parentheses for grouping expressions. So even though the trailing comma may seem optional, it is required to indicate that weare creating a tuple with a single element.

Without the trailing comma, Python would interpret the expression (42) as an integer enclosed in parentheses, rather than as a tuple.
# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
Ans: 

To convert a list to a tuple in Python, the tuple() function needs to be used.

For example, below the tuple() function is used to convert my_list to a tuple, resulting in my_tuple. The tuple() function takes an iterable (in this case, the list) as an argument and returns a tuple containing the elements of the iterable.


my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)
#Output = (1, 2, 3, 4)


To convert a tuple to a list, we can use the list() function. 
For example below, the list() function is used to convert my_tuple to a list, resulting in my_list. The list() function takes an iterable (in this case, the tuple) as an argument and returns a list containing the elements of the iterable.


my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print(my_list)
#Output = [1, 2, 3, 4]


# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
Ans: 

Variables that "contain" list values in Python are actually referencing the list objects rather than containing them directly. In Python, variables are references to objects in memory.

When you assign a list to a variable, the variable holds a reference to the memory location where the list object is stored. This means that the variable "points" to the list object rather than directly containing the list data.

For example:

my_list = [1, 2, 3]

In the code above, my_list is a variable that references a list object containing the elements [1, 2, 3]. The variable my_list does not contain the list directly but holds a reference to the list object in memory.
# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans: 

copy.copy() creates a shallow copy where nested objects are referenced, while copy.deepcopy() creates a deep copy where all nested objects are recursively copied. 

copy.copy():
The copy.copy() function creates a shallow copy of an object. Shallow copy means that it creates a new object, but the contents of the new object are references to the same nested objects as the original. If any of the nested objects are modified, the changes will be reflected in both the original and the copied object.

copy.deepcopy():
The copy.deepcopy() function creates a deep copy of an object. Deep copy means that it creates a new object and recursively copies all nested objects within the original object. This ensures that changes made to nested objects in the copied object do not affect the original object.