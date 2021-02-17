# the @decorator_name in Python and are called in bottom-up fashion. For example:
# decorator function to convert to lowercase
# def lowercase_decorator(function):
#     def wrapper():
#         func = function()
#         string_lowercase = func.lower()
#         return string_lowercase
#     return wrapper

# decorator function to split words
# def splitter_decorator(function):
#     def wrapper():
#         func = function()
#         string_split = func.split()
#         return string_split
#     return wrapper
#
# @splitter_decorator	# this is executed next
# @lowercase_decorator	# this is executed first
# def hello():
#     # print("hello feroz")
#     return'Hello World'
# hello() 	 # output => [ 'hello' , 'world' ]
# print(hello)
# print(id(hello))

a = [1, 2, 3]
b = [7, 8, 9]

n=[(x+y) for (x,y) in zip(a,b)]#parallel iterator
print(n)

z=[(x,y) for x in a for y in b]  #nested iterator
print(z)


my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]
print(squared_list)# list comprehension
# output => [4 , 9 , 25 , 49 , 121]

squared_dict = {x:x**2 for x in my_list}
print(squared_dict)# dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
# Performing conditional filtering operations on the entire list
my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list if x%2 !=0]
print(squared_list)# list comprehension
# output => [9 , 25 , 49 , 121]



squared_dict = {x:x**2 for x in my_list if x%2 != 0}    # dict comprehension
# output => {11: 121, 3: 9 , 5: 25 , 7: 49}

## generate fibonacci numbers upto n
def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q

# x=fib(10)
# x.__next__()
# x.__next__()
#
for i in fib(100):
    print(i)#
# ****************************
def fib(n):
    x,y=0,1
    while(x<n):
        yield x
        x,y=y,x+y

for i in fib(200):
    print(i)


__author__ = "Narendra Boyina"

__author__ = "Narendra Boyina"
"""
Explain the use of decorators.
Ans: Decorators in Python are used to modify or inject code in functions or classes. 

Using decorators, you can wrap a class or function method call 
so that a piece of code can be executed before or after the execution of the original code.
 Decorators can be used to check for permissions, modify or track the arguments passed to a method, 
 logging the calls to a specific method, etc.




 Higher Order Functions :
 =======================
 A function which takes other functions as its argument is called higher Order Function.

 Example:
 Decorators provide a simple syntax for calling higher-order functions.
 By definition, a decorator is a function that takes another function and it
 extends the behavior of the latter function without explicitly modifying it
"""


# def students(new_student):
#
#     # The original list of students
#     students_list = ["Sindhu", "Dev", "Hanumanth", "Sravya","Jithendra"]
#     print ("The original list of students is : ", students_list)
#
#     # Calling the function of new student
#     student = new_student()
#
#     # Appending the new student to the original list
#     students_list.append(student)
#
#     # The updated list of students
#     print("The updated list of Students is :  ", students_list)
#
#
# @students
# def new_student():
#     new_stud = input("Enter the new students name : ")
#     # print("The new student is :  ",new_stud)
#     return new_stud
#
# # This can be interpreted as
# students = students(new_student)

# def decor(fun):
#     def innner():
#         result = fun()
#         return result *2
#     return innner
#
# @decor
# def num():
#     print("number is 20")
#     return 20
#
# print(num())

# """