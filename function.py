# # Method:
# # Function which is declared inside the class is nothing but Method
# # Both Function and Method is similar in the application and function
#
# # Function syntax:
# # set of instruction Executed repeatedly
# # def function name():define a function with def keyword and function as its name
# #  call function
# # functionname(): we can  call this in any line after defining the function
# # In general practice we initialize as follows:
# # a=6;b=9;
# # c=a+b;
# # print(c)# This is logic we dont want to write again and again the block of logic where it is in use
# # #Better we go for def keyword
# # for Example:
# #Declared Function
# # def addition():#  def is a keyword addition is a function we are defining
# # # A function name to uniquely identify the function.
# # # Function naming follows the same rules of writing identifiers in Python.;
# # #Parameters (arguments) through which we pass values to a function. They are optional
# #       a=45;
# #       b=40;
# #       c=a+b;
# #       print(c)
# #call the function addition():
# #call the function  set of instruction going to Execute:
# def addition():
#     print("addition")
# addition()# calling the fucntion when ever required
# #Declared the Function with arguments (Different set of inputs)
# # addition()#------>a=7,b=3;
# # addition()#------>a=5,b=5;
# # addition()#------>a=2,b=3;
# def addition():
#     a=25;b=20;
#     c=a+b;
#     print(c)
# addition()
# def greet(feroz):
#
#     print("hello",feroz," Good morning!")
# greet("feroz")
# def addition(a,b):
#     sum=(a+b)
#     div=(a/b)
#     mul=(a*b)
#     sub=(a-b)
#     floor=(a//b)
#     return sum,div,mul,sub,floor
#     # print(addition(a,b))
# print(addition(4,4))
# result=addition(20,5)
# print(result)
# def add_sub_div(a,b):
#     c=a+b
#     d=a-b
#     e=a/b
#     return c,d,e
# result=add_sub_div(5,6)
# print(add_sub_div(2,2))
# for i in result :
#     print(i)
# print(type(result),result)
# print(add_sub_div(10,2))
# s=add_sub_div(20,2)
# for i in s:# iteration of result or variable
#     print(i)
# functions in which arguments types as follows
# 1)Required positional arguments
# 2)keyword arguments are mapping or dictionary type wherev key with  value
# 3)default arguments
# 4)variable length arguments
# Required arguments
# while defining a function the arguments passed should as same wile calling a function
# for example as follows:
# def employee_details(name,id):
#     name="feroz"
#     print(name,id)
#     print(name)
#     print(id)
#
# # employee_details("feroz")#TypeError: employee_details() missing 1 required positional argument: 'id'
# employee_details("feroz",240)
# *******************************************
# keyword arguments :
# function defining  arguments and function calling  arguments should be in sequence
# for example as follows
def client_details(name, id, sal, address):
    print("name:",name)
    print("id :",id)
    print("sal :",sal)
    print("address :",address)
    return name,id,sal,address
result=client_details("kursheed",2006,20000,"cpt")
print(result)
for i in result:
    print(i)


client_details("feroz",2010,45000,"bangalore")# we are defining all in sequence
# def client_details(name, id, sal, address):
#     print("name",name)
#     print("id",id)
#     print("sal",sal)
#     print("address",address)
# client_details(2010,"feroz",45000,"bangalore")#we are defining but calling without order
# # that is key with according value should be written in order
#**default arguments**##
# when defining a function if intilize the arguments with some variable example as follows
# def add(a,b,c=0):
#     total=a+b+c
#     return total
# print(add(10,20))# it wont through error that missing 1 argumnet
# print(add(10,20,10))# if you give value it will take and execute
##############################################
# variable length argument
# def printme(*arg,**Kwarg):

# def printinfo(arg1,*vartuple):
#         print("arg1 is",arg1)
#         print(vartuple)
#         for var in vartuple:
#
# print("var tuple arg is",arg1)
#         return
#         print("return")
#
# printinfo(50,60,40,50,90,"feroz")

#*******************************************####
#befroe the above code to execute we have to know the *args ,**kwargs
# args are only values where as kwargs is keyvalues
#while defining a function having  0 to  n number of values we intilize as *args
# where as keyvalues that is from 0 to n **kwargs
# for example for args with n number
# def add(*args):
#     add=args
#     print(add)
# print(add(10,20,30))
# def mobile_model(**kwarg):
#     print("model no:",**kwarg)
#     print("config",**kwarg)
#     print("os.version",**kwarg)
#     print("brand",**kwarg)
# mobile_model()#doubt to ask to harsha



# def myname():
#     print("Myname is feroz")
#     x=print("My fatther name is saida")
#     print(x)
#     print(type(x))
# myname()
# def addition(a,b):
#     c=a+b
#     print(c)
#
# addition(2,3)
# def subtraction(a,b):
#     print(a-b)

# subtraction(10,2)
# subtraction(3,2)# we have to call the function after defining with keyword def and function name as substraction \n
# # logic within print function
# def division(a,b):
#     print(a%b)
#
# division(8,2)
# def multiplication(a,b):
#     print(a*b)
# multiplication(5,2)
# def floordivision(a,b):
#     print(a//b)
# floordivision(10,6)
# def sumof(a,b):
#     print(a+b)
# sumof(2,3)

#return keyword
# def addition(x,y):
#     c=a+b
#     print(c)
# addition(4,5)
# return c
# print(addition(4,5))
# result=addtion(8,4)
# print(result)

# #Decalre function with one return multiple values
# def addition(a,b):
#     sum=(a+b)
#     div=(a/b)
#     sub=(a-b)
#     mul=(a*b)
#     return sum,div,sub,mul
# print(addition(4,4))
# result=addition(5,5)
# print(result)
# print(type(result))# the result make the value in tuple
# see th follow code with result
# def addition(a,b,c):
#     """
#
#     :type c: object
# #     """
# def mathoperation(a,b,c):
#     print(a+b+c)
#     sum=a+b+c
#     div=a/b/c
#     sub=a-b-c
#     mul=a*b*c
#     return sum,div,mul,div
# result=mathoperation(10,5,2)
# print(result)

# mathoperation(12,15,30)

# def addition(a,b,c,d):
#     print(a+b+c+d)
# addition(4,5,5,2)# function with arguments assined

# Function with variable length(*n), number of variables
# def addition(*n):# we can pass 'n' number of variables/values
#      print(n+n)
#
# addition(34,85)# addition(15,"feroz")
# result=addition(2,5,6,8)
# print(result)
# def mul(*n):
#     print(*n)
# mul(2)
#mul function throughing error like this how to slove this issue
# # TypeError: can't multiply sequence by non-int of type 'tuple'
# def div(*n):
#     print(n%n)
# div(5,5)
# div(5,2)#TypeError: unsupported operand type(s) for %: 'tuple' and 'tuple'

# n----->number of variable
# function based on one variable and length -keywword (Dictinary)
# def feroz(**n):
#     print(n)
# feroz(name="feroz feroz feroz feroz feroz",address='chuttugunta',phone=6304670341)# output is key and values as dictionat or mapping
#
# def imthiyaz(**n):
#     print(n)
# imthiyaz(loaction="hyderabd",employee="cylient",native="gunturian")

# Recursion is a process of function calling itself
# good example is a fcatorial of a number
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
# # another way of getting factorial with slight change
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
#
# print(factorial(100))


# 1.What is  mean by functions in python?
# function we can define with keyword def and call with in function
# syntax:
# def function():
# advantage of function as follows
# Re-uasable,Modularity,Maintenance
# 2.What are the types of functions?
# functions,functions with arguments,functions with return type
# 3.How will you declare the functions?
# def function():
# 4.How many values it will return?
# n number of values in the instruction under the function
# 5.What is the use of * operator in python functions?
# Operators are special symbols in Python that carry out arithmetic or logical computation
# 6.What is lambda function in Python?
# Anonymous function (Arithimatic) to reduce the code of the program
# 7.What is a recursive function?
# recurssion is the process of function calling itself
# 8.What is an anonymmous function?
# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python
# anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions\n
# 9.What is  differencce between filter() and map()?
# 10.What is reduce() and in which module it is present?
# 11.What is keyword used for function deceleration?
# 12.What is use of ** operator in python functions?
# 13.What is difference between * and ** functions?
# 14.Can we able to change value of global variable?

# ********************************************************
# Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".
#
# 1. map() :
# map() will apply the function to every item of iterable and return a list of the results.
# Syntax :
# map(function, iterable, ...)
#
#
# 2. filter() :
# The function filter(function, list) offers an elegant way to filter out all the elements of a list,
# for which the function function returns True.
#
# 3. reduce() :
# The function reduce(func, seq) continually applies the function func() to the sequence seq.
# It returns a single value.

#Anonymous Function :
# (Arthimetic)
# # without name ,one time usage,reduce the code
# v=lambda x:x*x# lambda keyword
# print(v(8))# passing ane variable
# v1=lambda x,y:x/y
# print(v1(5,2))#passsing two variable
# x=lambda x,y,z:x+y+z/3
# print(x(5,2,3))#passing three variables
#cube of a number
# def cube(n):
#     return n**3
# print(cube(2))# its  normal like function calling
# f=lambda n:n**3#
# print(f(2))
# #create a number if even true and if odd false with a lambada keyword
# l=lambda x:"yes"if x%2==0 else "no"
# print(l(10))

#lambda that will calculate sum of two numbers
# y=lambda x,y:x+y
# print(y(2,3))


# Filters function filter(lambda,lst)
# lst=[10,20,15,17,18,12]
# l=filter(lambda x:x%2==0,lst)# we have to convert it to list
# y = list(filter(lambda x: x%2==0,lst))
# x = list(filter(lambda y: y%2==1,lst))
# print(y)
# print(x)
# for i in x:print(i)#we want iterate the list out of the fucnction

# What is  differencce between filter() and map()
#advantage of filter function to filter the data from the database
# mapping function
# lst=[2,5,6,8]
# l=list(map(lambda n:n*2,lst))# map function used to double the number
# s=list(map(lambda m:m%3,lst))#convert the map into list
# print(l)#to know the type
# print(type(l))
# print(s)

# l=list(map(lambda n:n*2,lst))#convert to list
# print(l)
# for i in l:print(i)# we can iterate the
# x=list(map(lambda y:y**3,lst))#we acn use logic of cube of numbers
# print(x)
# n=list(map(lambda m:m%2,lst))
# print(n)

# What is reduce() and in which module it is present?
#reduce function we have to import it from functiontools as follows
# from functools import reduce
# lst=[4,5,20,50]
# l=reduce(lambda x,y:x+y,lst)
# x=reduce(lambda x,y:x*y,lst)
# print(l)
# print(x)



# local and global varaibles
#local variables within function
# global variables are out of function
# def details():
#     x=20#local variable or value within function gives  priorty for loacal variable
#     print(x)
# details()

# x=99
# def details():
#     x=45
#     print(x)
#     print(globals()['x'])#Get the global varaible which is outside the function
#     print(globals().get('x'))
# details()
#
y=85
# def feroz():
#     y=52
#     print(y)
#     print(globals()['y'])
#     print(globals().get('y'))
# feroz()
# details()# calling the anothing function within another function
# Scope of the variable of local is within the function
# x=120
# def details():
#     x=105
#     print(x)
# details()
#
# def addition():
#     print(globals().get('x'))
#     print(globals()['y'])
# addition()# we cannot call the x variable in the addition that  is in another function  because
# # it is local variable
#
# def details():
#     global x
#     x=20# local varaiable to convert into global varaiable as follows
#     print(x)
# details()
# def addition():
#     print(x)
# addition()
# details()
# addition()

# important function
# 1)filters() 2)map() 3) reduce()
#print only even number
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#         l=[10,12,14,16]
# is_even(10)# doubts to be asked to raseem
# lst=[2,10,15,20]
# l=list(filter(lambda x:x%2==0 ,lst))#above filter function can be written as follows
# print(l)
#
# print(list(filter(is_even(l)))#doubt to ask raseem sir

# Mapping
# l=[2,3,4,5,6]
# def square_it(x):
#     for x in l:
#         l = [2, 3, 4, 5, 6]
#         print(x*x)
#
# square_it(2)doubt to be asked to raseem
# Functions  : greens_Omr(),greens_Adayar(),greens_Tambaram(),greens_Velacherry(),greens_Anna_Nagar()
#
# Description: Create the above functions with passing some arguments
# def greens(x,y,z,a,b,c,):
#     greens_omr=(x+y)
#     greens_Adayar=(a-b)
#     greens_Tambaram=(c)
#     return greens_omr,greens_Adayar,greens_Tambaram
# print(greens(1,2,3,4,5,6))

# QUESTION 3.1:
# -------------
# Description:Find the output for the below function

# def my_function(fname, lname):
#    print(fname + " " + lname)
#    print(fname , lname)
#
# my_function("Harry","")#TypeError: my_function() missing 1 required positional argument: 'lname'
# Create a recursive function of your own and print the word "python" upto 100 times
# def python(n):
#     if n==0:
#         return 1
#     else:
#         python=*(n-1)
# python(python)

# ******************************************************
# for i in range(4):
#     print("#  ",end=' ')
# print()
# for j in range(4):
#     print("#  ",end=' ')
# print()
#
# for k in range(4):
#     print("#  ",end=' ')
# print()
# #################
# # better to make less code of above one as follows
# for i in range(4):
#     for j in range(4):
#         print("#  ",end='  ')
#
#     print()
# for i in range(6):# half triangle with the for loop code:
#     for j in range(i):
#         print("#  ",end='  ')
#
#     print()
# **********************************************************************
_author__ = "Harsha Vardhan"

# Recursive function & Non-recursive functions
#01 CALLING A FUNCTION
''' Calling a Function
Defining a function gives it a name,
 specifies the parameters that are to be included in the function and 
 structures the blocks of code.

Once the basic structure of a function is finalized,
 you can execute it by calling it from another function or directly from the Python prompt.
  Following is an example to call the printme() function −
'''

# function without arguments


# def print_my_info( ):
#    print("Harsha")
#    print("Surendra and Aruna")
#    return "Harsha"
#
#
# print(print_my_info())
# print_my_info()  # the purpose of function is code reusability


# function with positional arguments

# def Email(a, b):
#    "This prints a passed string into this function"
#    print(a+"."+b+"@gmail.com")
# #
# #Now you can call printme function
# Email("Vardhan","Harsha")   # programmer friendly
# x= input("Enter first name")
# y = input("Enter last name")
# Email(x,y)   # user friendly


# ''x
i = 10
list = [1,2,2,4]
# Pass by Reference vs Value
# All parameters (arguments) in the Python language are passed by reference. It means if you change
# what a parameter refers to within a function, the change also reflects back in the calling function. For example −
# '''
#
#
# ## 02 We can call a function in 2 way
# #01 Call by value

# #03 CALL BY VALUE
# # Function definition is here
# #
# def change_me(mylist):
#    "This changes a passed list into this function"
#    print ("Values inside the function before change: ", mylist)
#    mylist = [1, 2, 3, 4] # This would assign new reference in mylist
#    print("Values inside the function: ", mylist)
#
# # Now you can call changeme function
# mylist = [10,20,30]
# change_me(mylist)
# print ("Values outside the function: ", mylist)
#
# '''
# The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist.
# The function
# accomplishes nothing and finally this would produce the following result −
# Values inside the function:  [1, 2, 3, 4]
# Values outside the function:  [10, 20, 30]





#02 Call by reference

# Function definition is here
#
# def change_me( mylist ):
#    "This changes a passed list into this function"
#    print ("Values inside the function before change: ", mylist)
#    mylist[2]=50
#    print ("Values inside the function after change: ", mylist)
# #    return
# # #
# # # Now you can call changeme function
# mylist = [10,20,30]
# change_me(mylist)
# print("Values outside the function: ", mylist)

# '''
# Here, we are maintaining reference of the passed object and appending values in the same object.
# Therefore, this would produce the following result −
#
# Values inside the function before change:  [10, 20, 30]
# Values inside the function after change:  [10, 20, 50]
# Values outside the function:  [10, 20, 50]
# There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function.
# '''
#
#

# '''
# #NOTE: when you call by reference the value outside the function gets changed
#
# '''
# Function Arguments
# You can call a function by using the following types of formal arguments −
#
# 01 Required arguments
# 02 Keyword arguments
# 03 Default arguments
# 04 Variable-length arguments
# '''
#
# '''
# 01 Required Arguments
# Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments
# in the "function call" should match exactly with the "function definition".
#
# To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows−
# '''
#
# # # Function definition is here


# def print_me(s, a, c):
#     """This prints a passed string into this function"""
#     print(s, a, c)
#     return
#
# Now you can call printme function
#print_me(12,23,22)
#print_me(3,5)
# 2
# '''
# OUTPUT:
# When the above code is executed, it produces the following result −
#
# Traceback (most recent call last):
#    File "test.py", line 11, in <module>
#       printme();
# TypeError: printme() takes exactly 3 argument (2 given)
# '''
#
#
# '''
# 02 Keyword Arguments
# Keyword arguments are related to the function calls. When you use keyword arguments in a function call,
#  the caller identifies the arguments by the parameter name.
#
# This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the printme() function in the following ways −
# '''
#
# # Function definition is here

#
# def keyword_arg(name ,age,sal):
#    print("Name is:",name)
#    print("age:",age)
#    print("sal:", sal)
#
# keyword_arg("Harsha",32,10000)
# keyword_arg(32,"harsha", 1000)

# # '''
# When the above code is executed, it produces the following result −
#
# My string
# The following example gives a clearer picture. Note that the order of parameters does not matter.
# '''
#

# # Function definition is here
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age :", age)
#    return
#
# # # Now you can call printinfo function
# printinfo( age = 27, name = "Harsha" )
# printinfo( 27, "Harsha")
# '''
#
# '''
# 03 Default Arguments
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
# The following example gives an idea on default arguments, it prints default age if it is not passed −
# '''
#
# #!/usr/bin/python3
# # Function definition is here
# def printinfo( name, age=35 ):
   # "This prints a passed info into this function"
   # print ("Name: ", name)
   # print ("Age ", age)
   # return
#
# # Now you can call printinfo function
#printinfo()
#printinfo( "Harsha ")
#printinfo( "Surendra",28)
#printinfo("Sri")


#
# def abc(c, d, a=24, b=10):
#    print(a,b,c,d)
#
#    return

# abc(12, 24)

#
'''
 04 Variable-length Arguments
 You may need to process a function for more arguments than you specified while defining the function. 
 These arguments are called variable-length arguments and are not named in the function definition, unlike 
 required and default arguments.
 Syntax for a function with non-keyword variable arguments is given below −
'''
# def functionname([formal_args,], *var_args ):
#    "function_docstring"
#    function_suite.
#    return [expression]

# An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.
# This tuple remains empty if no additional arguments are specified during the function call.
# Following is a simple example −
#
# Function definition is here
#
# here
# def printinfo(arg1, *vartuple):
#    """
#    this function performs variable length arguments
#    other than 1st argument remaining values will be stored in tuple
#    """
#    print("arg is: ", arg1)
#    print(vartuple)
#
#    for var in vartuple:
#       print("Var_tuple  arg is", var)
#    return
#
# Now you can call printinfo function
#printinfo()      #  TypeError: printinfo() missing 1 required positional argument: 'arg1'
# printinfo(10)
# printinfo(60, 70)
#printinfo(50, 60, 70)
#printinfo(50, 60, 70,49,30,279,"Narndra",78, 67.87)

#
# def add(a, *b):
#    print("addition of and b is :", a,b)
#    for v in b:
#       a = a+v
#    print(a)
# # #
# add(2,3,4,5,3,4,5,6,7)


# '''
# When the above code is executed, it produces the following result −
#
# Output is:
# 10
# Output is:
# 60
# 70
# Output is:
# 50
# 60
# 70
# '''

# def f(*args,**kwargs):
#   print(args, kwargs)
# # #
# l = [1,2,3]
# t = (4,5,6)
# d = {'a':7,'b':8,'c':9}
#
#f()
#f(1,2,3)                    # (1, 2, 3) {}
#f(1,2,3,"groovy",2.5)           # (1, 2, 3, 'groovy',2.5) {}
#f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
#f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
# f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}
#
# f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
# f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
# f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
# f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
# f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
# def Harsha(x,*y,**z):
#   print(x)
#   print(*y)
#   print(**z)
#
# Harsha(1,2,3,4,5,"Bhagyasree",x =11, y=12,z=13)
# # Important :
# # ==========

#
# # output: TypeError: Harsha() got multiple values for argument 'x'
#
# #
# def cal(a,b,x):
#     c =a + b
#     d = a*b
#     x += 10
#     print(c)
#     print(d)
#     print(x)
#     return c,d,x
# renuka, veeraj,Siva = cal(2,3,4)
# printinfo(renuka,veeraj,Siva)

# *****************************************************************************
#  Definition of function is a group of statements that will perform a perticular task
# execute by calling function.
# """
# """                                         The  Main Advantage Of Function Is Code Re-Usability                                    """
# # example function without arguments
#
# def exmpl():
#     print("hi this is karthik")
#     print("this is example of function without argument")
# exmpl()
# """
# hi this is karthik
# this is example of function without argument
# """
# ############  function with positional arguments
#
# def print_me(a, b):
#     print(a + "." + b +"@gmail.com")
# print_me("kola", "karthikrishna")
# print_me("kola", "sravani")
# print_me("kola", "deethu")
# print_me("kola", "divi")
# #  the above program is programmer friendly program.
#
# # the below program is user friendly program.
#
# def my_info(x, y):
#     print(x+"."+y+"@yahoo.com")
#
# x = input("enter firsh name:")
# y = input("enter second name:")
# my_info(x, y)
# # here ask input to user in execution time
#
# ############# function call by value example
#
# def change_info(mylist):
#     print("values inside before change:", mylist)
#     mylist = [1,2,3,4,5]
#     print("inside values after change:", mylist)
#     mylist[4] = 60
#     print("inside values after change:", mylist)
#     return
# mylist = [10,23,43]
# change_info(mylist)
# print("outside of the values:", mylist)
# #  o/p:values inside before change: [10, 23, 43]
# # inside values after change: [1, 2, 3, 4, 5]
# # outside of the values: [10, 23, 43]
#
# def value_chg(mylist):
#     print("values inside before change:", mylist)
#     mylist[4] = 50
#     print("values ofter change:", mylist)
#     return
# mylist = [10,20,30,40,60]
# value_chg(mylist)
# print("outside of the list:", mylist)
# # o/p: values inside before change: [10, 20, 30, 40, 60]
# # values ofter change: [10, 20, 30, 40, 50]
# # outside of the list: [10, 20, 30, 40, 50]
#
# """
# ##  Funtional arguments
# # you can call by function by using fallowing types of formal arguments.
# # 1. required arguments
# # 2. keyword arguments
# # 3. default arguments
# # 4. variable length arguments
#
# #############  Required arguments
#
# """
# def rqrd_armnt(a, b, c):
#     ''' "example of required arguments " '''
#     print(a, b, c)
#     return
# rqrd_armnt(12,13,"kkk")  # o/p: 12 13 kkk
#
# def keyword_args(a, b, c): # keyword arguments are the call by parameter in function.
#     print(a)
#     print(b)
#     print(c)
#     return
# keyword_args(12,13,24)  # o/p: 12 13 24 line by line
# keyword_args(15,12,c=13)  #  o/p:  15,12,13
#
#
# def my_info(name, age):
#     print("name:", name)
#     print("age:", age)
#     return
# my_info("karthik", age=68 )
# my_info(23, 59)
# #o/p:
# # name: karthik
# # age: 68
# # name: 23
# # age: 59
#                                                ###############   Default arguments ##############
#
#
# """default arguments are the assign a value to argument defaultly that works when you not given the value of argument in fonction call
#    then it will take default value."""
#
# def deflt_argmts(name, age=45):
#     print("name:", name)
#     print("age:", age)
#     return
# deflt_argmts("farith")
#
# # o/p: name: farith
# # age: 45
#
# def dearg(c, d, a=12, b=34):
#     print(a)
#     print(c)
#     print(d)
#     print(b)
#     return
# dearg(1,d=22)
# """
# o/p: 12
# 1
# 22
# 34
# """
# '''                                            VARIABLE LENGTH ARGUMENTS.                                                  '''
# def ver_len(arg1, *args):
#     print("formal argument is:", arg1)
#     print("variable tuple is:", args)
#     return
# ver_len(10,23,24,25,"kkk","Greenstechno")
# #   o/p: formal argument is: 10
# # variable tuple is: (23, 24, 25, 'kkk', 'Greenstechno')
# ver_len(10,20)
# """
# o/p: formal argument is: 10
# variable tuple is: (20,)
# """
# def add(a,*b):
#     print("addition of a and b is:", a, b)
#     for v in b:
#         a += v
#         print(a)
#     return
# add(2,3,4,5,3,4,5,6,7)
# '''
# O/P: 5
# 9
# 14
# 17
# 21
# 26
# 32
# 39
# '''
#
# def f(args1, *args, **kwargs):  # here args1 is farmal value , *args ia variable tuple, **keywordargs is dictionary
#     print(args1, args, kwargs)
#     return
# l = [1,2,3,4]
# t = (6,7,8,9,10)
# d = {"a" : "k1", "b" : "k2", "c" : "k3"}
#
# f(1,2,3,4,5,6,34,3,5,2.5)   # o/p: 1 (2, 3, 4, 5, 6, 34, 3, 5, 2.5) {}
#
# f(123, l, 23, 35, 65, g=23, *t, **d)  # 123 ([1, 2, 3, 4], 23, 35, 65, 6, 7, 8, 9, 10) {'g': 23, 'a': 'k1', 'b': 'k2', 'c': 'k3'}
#
# f(l,123,234,45,56,65,*t,**d,farith=26)   # [1, 2, 3, 4] (123, 234, 45, 56, 65, 6, 7, 8, 9, 10) {'a': 'k1', 'b': 'k2', 'c': 'k3', 'farith': 26}
#
# f(1,2,3,h=45,t=34)  #  1 (2, 3) {'h': 45, 't': 34}
#
# def cal(a,b,x):
#     c =a + b
#     d = a*b
#     x += 10
#     print(c)
#     print(d)
#     print(x)
#     return c,d,x
# bhaskar, karthik, sravani = cal(2,3,4)
# #5
# # 6
# # 14
# print(bhaskar, karthik, sravani) # o/p: 5 6 14
#
# ### lambda function
#
# # First we pass the arguments and then the expression or logic
#
# """
# 1)These functions are called anonymous because they are not declared in the standard manner
# by using the "def" keyword.
# 2)You can use the lambda keyword to create small anonymous functions.
# 3)Lambda forms can take any number of arguments but return just one value in the form of an expression.
# They cannot contain commands or multiple expressions.
# An anonymous function cannot be a direct call to print because lambda requires an expression.
#
# """
#
#
# # lambda Function expression
# # varible = lambda arguments: operation
# # Syntax:  variable = lambda [arg1 [,arg2,.....argn]]:expression
# # Note: variable works as a function name
#
#
# # it will give one value
# bharath = lambda arg1 , arg2 : arg1*arg2
# print(bharath(10,4))
# #  o/p: 40
# # 2. Map Function
# # =============
#
# """
# map() :
# map() will apply the function to every item of iterable and
# return a list of the results.
# (or)
# Map means Apply same function to each element of a sequence
# Map returns the modified list.
#
# Syntax :
# map(function, iterable, ...)
# """
# # # Ex : Create a list of squares for the first 5 numbers
#
# numbers = range(5,9)
# # nos = range(1,4)
# # squares = map(lambda x : x**x, numbers)
# # print(squares)  # it will give object only because have not convert in to list. it will display input when its converts list
# # o/p: <map object at 0x005CD310>
# squares = list(map(lambda x : x**x, numbers))
# print(squares)  #o/p: is [3125, 46656, 823543, 16777216]
#
# l = ['sat', 'bat', 'cat', 'mat']
# #
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
#
# # Filter Function:
# # ================
#
# """
# 3. filter() :
# The function filter(function, iterable) offers an elegant way to filter out all the elements of a list,
# for which the function function returns True.
# (or)
# Filter items out of a sequence
# returns filtered list
# """
# def is_even(x):
#     if x%2 == 0:
#         return x
# nums = range(20,40)
# x = filter(is_even, nums)
# print(x)
# x = list(filter(is_even, nums))
# print(x)
#
# ###############   ZIP function
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = ["s","s1","s3","s4","s5","s6"]
# zip_list = zip(l1, l2)
# # print(zip_list)
# # print(list(zip_list))
# c = list(zip_list)
# # print(c)
#
# l3= ["aaa1","qqq", "kkk", "kle", 2.5, 789]
# dw = list(zip(l1,l2,l3))
# # print(dict(dw))
# k1,k2,k3 = zip(*dw)
# # print(k1)
# # print(k2)
# # print(k3)
#
# # for x,y in zip(l1,l3):
#     # print(x, "-->", y)
#
# # for i, (a,b) in enumerate(zip(l2,l3)):
#     # print(i+1,a,b)
#
#
# dw.sort(key = lambda x: x[1])
# # print(dw)
#
# cube = lambda x:x**3
# # print(cube(3))
# # print(cube(456))
# ########## by use lambda function we can reuse so many times.
# list1= [1,2,3,4,5,6,7,8,9,456,1321,84654,5534,64561,65131,64564]
# listeven= list(filter(lambda n:n%2==0,list1))
# print(listeven)
# listodd=[]
# for i in list1:
#     if i%2==0:
#         listeven.append(i)
#     else:
#         listodd.append(i)
# print(listeven)
# print(listodd)
# *****************************************************************
__author__ = "Narendra Boyina"

# functions continuation (class 2) and lambda function

"""
The return Statement
The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

All the examples given below are not returning any value. You can return a value from a function as follows −
"""
#
# Function definition is here
# def sum_mul( arg1, arg2,arg3 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2 + arg3
#    m = arg1 * arg2 * arg3
#    print ("Inside the function : ", total)
#    print("Inside the function : ",m)
#    return total,m
#
# # # Now you can call sum function
# total,m = sum_mul( 10, 20,30 )
# print ("Outside the function : ", total )
# print ("Outside the function : ", m )



"""
Scope of Variables
All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes
 of variables in Python −

1. Global variables
2. Local variables

#Global vs. Local variables
Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.
This means that local variables can be accessed only inside the function in which
they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, 
the variables declared inside it are brought into scope. Following is a simple example −
"""
#
# total = 100 # This is global variable.
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total2 = arg1 + arg2 # Here total is local variable.
#    print ("Inside the function local total : ", total2)
#    return total2
# #
# # # Now you can call sum function
# total4 = sum( 10, 20 )
# print("Outside the function global total : ", total)
# print(total4)
#

"""
Usage of help() and dir() function in Python?
Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 

Help() function: The help() function is used to display the documentation 
===============  string and also facilitates you to see the help related to modules, keywords, attributes, etc.
Dir() function: The dir() function is used to display the defined symbols.
===============
"""
# print(help(max))
# print(input)

### lambda function

# First we pass the arguments and then the expression or logic
"""
1)These functions are called anonymous because they are not declared in the standard manner 
by using the "def" keyword.
2)You can use the lambda keyword to create small anonymous functions.
3)Lambda forms can take any number of arguments but return just one value in the form of an expression. 
They cannot contain commands or multiple expressions.
An anonymous function cannot be a direct call to print because lambda requires an expression.

"""


# Function definition is here
# varible = lambda arguments: operation
# Syntax:  variable = lambda [arg1 [,arg2,.....argn]]:expression
# Note: variable works as a function name


# Bharath = lambda arg1, arg2 : arg1 + arg2*2
# print(Bharath)  # it will give the memory location because you have not a passed any inputs
# #
# # # calling function
# print("Value of total : ", Bharath(10, 20))
# print("Value of total : ", Bharath( 20, 30 ))

# c = lambda a, b: a**b
# # # # print(c)  # it will give the memory location because you have not passed any inputs
# #
# # calling function
# print(c(2,3))
# print(c(2,6))



# 2. Map Function
# =============

"""
map() :
map() will apply the function to every item of iterable and 
return a list of the results.
(or)
Map means Apply same function to each element of a sequence
Map returns the modified list.

Syntax :
map(function, iterable, ...)
"""
# # Ex : Create a list of squares for the first 5 numbers

# numbers = range(1,6)
# squares = map(lambda x: x*x, numbers)
# squares = list(map(lambda x: x**x, numbers))
# # #
# print(squares)


# Note:- Need not necessarily use a lambda function print(list(map(square, iterable)))

# Filter Function:
# ================

""""
3. filter() :
The function filter(function, iterable) offers an elegant way to filter out all the elements of a list, 
for which the function function returns True. 
(or)
Filter items out of a sequence
returns filtered list
"""
# Ex: Print only the even numbers from 20 to 40
#
# def is_even(x):
#     if (x % 2 == 0):
#         return x
#
# numbers = range(20, 40)
# x = filter(is_even, numbers)
# x = list(filter(is_even, numbers))
# print(x)



# O / P: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

""" reduce()
Applies same operation to items of  a sequence
Uses result of operation as  a first parameter of next operation
returns an item, not a list"""
# from functools import reduce#we have to import the reduce from functiontools
# N = [5,4,2,3]
# print(reduce(lambda x,y:x*y,N))
# print(reduce(lambda x,y:x+y,N))
# print(reduce(lambda x,y:x/y,N))
# print(reduce(lambda x,y:x^y,N))
# ***************************************************



"""zip() function- it will take multiple lists say list1, list2, etc and transform them into a single list of tuples by taking the corresponding elements of the lists that are passed as parameters."""


# zip always creates the tuple in the order of iterables from left to right.
#  list_a will always be before list_b in the output tuples

# execute the below code in 2.7.x version it will give list of tuples.

# list_a = [1, 2, 3, 4, 5,8]
# list_b = ['a', 'b', 'c', 'd', 'e']
# # # # # #
# zipped_list = zip(list_a, list_b)   # execute only in python 2.7.x version
# print(zipped_list)
# print(list(zipped_list))

#

# In Python3, zip methods returns a zip object instead of a list. This zip object is an iterator.
# Iterators are lazily evaluated.
# Iterators returns only element at a time. len function cannot be used with iterators. We can loop over the zip object
#  or the iterator to get the actual list
# list_a = [1, 2, 3, 4, 5]
# list_b = ['a', 'b', 'c', 'd', 'e']
# # #
# zip_list = zip(list_a, list_b)
# # # #
# N = list(zip_list) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# print(N)
# B = list(zip_list) # Output []... Output is empty list because by the above statement zip got exhausted.
# print(B)
# #
#
# # zip with more than 2 lists

# list1 = ['A', 'B', 'C']
# list2 = [10, 20, 30,40]
# list3 = ["Narendra", "Surendra", "Aruna"]
# x = list(zip(list1, list2,list3))
# print(x)  # results in a list of tuples say [('A', 10, 'Narendra'), ('B', 20, 'Surendra'), ('C', 30, 'Aruna')]
# #
# #
# # # # """whenever the given lists are of different lengths, zip stops generating tuples when the first list ends"""
# A0 = dict(zip(('a','b','c','d','e','f'),(1,2,3,4,5)))
# print(A0)
# # #
# # # Unzip a list of tuples
# #
# # # To unzip a list of tuples we zip(*listP_of_tuples). Unzip creates separate list.
# # #
# zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# x, y = zip(*zipper_list)
# print("zipper list of x as follows",x)  # (1, 2, 3)
# print("zipper list of y as follows",y)  # ('a', 'b', 'c')

# For loop on zip concept
# Python program that uses zip on list

# items1 = ["blue", "red", "green", "white"]
# items2 = ["sky", "sunset", "lawn", "pillow"]
# list=items1.append(items2)
# print(list(gzip(items1,items2)))
# print(list)
# print(list(items1,items2))
# Zip the two lists and access pairs together.
# for x, y in list( zip(items1, items2)):
#     print(x, "==>",y)


# enumerate concept with zip
# Here is how to iterate over two lists and their indices using enumerate together with zip:
# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
# #
# for i, (a, b) in enumerate(zip(alist, blist)):
#     print(i, a, b)






#####**********    Practice Programs    *******####
"""Sorting a List of Tuples using Lambda"""
# list1 = [('eggs', 5.25), ('honey', 9.70), ('carrots', 1.10), ('peaches', 2.45)]
# list1.sort(key = lambda x: x[1])
# list1.sort(key=lambda y:y[0])
# print(list1)
# print(list1)
# # ans:[('carrots', 1.1), ('peaches', 2.45), ('eggs', 5.25), ('honey', 9.7)]

"""Sorting a List of Dictionaries using Lambda"""
# import pprint as pp
# list1 = [{'make':'Ford', 'model':'Focus', 'year':2013}, {'make':'Tesla', 'model':'X', 'year':1999}, {'make':'Mercedes', 'model':'C350E', 'year':2008}]
# list2 = sorted(list1, key = lambda x: x['year'])
# pp.pprint(list2)

# # Ans : [{'make': 'Tesla', 'model': 'X', 'year': 1999},
# #  {'make': 'Mercedes', 'model': 'C350E', 'year': 2008},
# #  {'make': 'Ford', 'model': 'Focus', 'year': 2013}]

# Ex : Find the cube of a given number

# cube = lambda x : x**3
# print(cube(2))
# print(cube(4))
# like lambda we can reuse lambda function so many time
# ****************************
# import pprint as pp
# listx=["hello world of python"]
# listy=["hello tester of selenium"]
# listn=print(zip(listx,listy))
# pp.pprint(listn)
#
# def say_hello(name1, name2):
#     return 'Hello ' + name1 + '! Hello ' + name2 + '!'
#
# say_hello('sara', 'ansh') 	 # output => 'Hello Sara! Hello Ansh!'
# print(say_hello('sara','ansh'))

# def myWrapper(n):
#     return lambda a : a * n
# mulFive = myWrapper(5)
# print(mulFive(2))


# ************************************************
# reverse the string using function
# def reverse(s):
#     s=str[::-1]
#     return s
#     # print(s)
#
# s="iam good at programming"
# print("The orginal string:",end="")
# print(s)
# print("the reveres of the string is:",end="")
# print(reverse(s))
# reverse(s)
# ******************************************************************

__author__ = "Narendra Boyina"

# functions continuation (class 2) and lambda function

"""
The return Statement
The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

All the examples given below are not returning any value. You can return a value from a function as follows −
"""
#
# Function definition is here
# def sum_mul( arg1, arg2,arg3 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2 + arg3
#    m = arg1 * arg2 * arg3
#    print ("Inside the function : ", total)
#    print("Inside the function : ",m)
#    return total,m
# #
# # # # Now you can call sum function
# total,m = sum_mul( 10, 20,30 )
# print ("Outside the function : ", total )
# print ("Outside the function : ", m )



"""
Scope of Variables
All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes
 of variables in Python −

1. Global variables
2. Local variables

#Global vs. Local variables
Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.
This means that local variables can be accessed only inside the function in which
they are declared, whereas global variables can be accessed throughout the program body by all functions. 
When you call a function, 
the variables declared inside it are brought into scope. Following is a simple example −
"""
#
# total = 100 # This is global variable.
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total2 = arg1 + arg2 # Here total is local variable.
#    print ("Inside the function local total : ", total2)
#    return total2
# #
# # # Now you can call sum function
# total4 = sum( 10, 20 )
# print("Outside the function global total : ", total)
# print(total4)
#

"""
Usage of help() and dir() function in Python?
Help() and dir() both functions are accessible from the Python interpreter and 
used for viewing a consolidated dump of built-in functions. 

Help() function: The help() function is used to display the documentation 
===============  string and also facilitates you to see the help related to modules, keywords, attributes, etc.
Dir() function: The dir() function is used to display the defined symbols.
===============
"""
# print(help(max))
# print(help(min))
# print(input)


### lambda function

# First we pass the arguments and then the expression or logic
"""
1)These functions are called anonymous because they are not declared in the standard manner 
by using the "def" keyword.
2)You can use the lambda keyword to create small anonymous functions.
3)Lambda forms can take any number of arguments but return just one value in the form of an expression. 
They cannot contain commands or multiple expressions.
An anonymous function cannot be a direct call to print because lambda requires an expression.

"""


# Function definition is here
# varible = lambda arguments: operation
# Syntax:  variable = lambda [arg1 [,arg2,.....argn]]:expression
# Note: variable works as a function name


# Bharath = lambda arg1, arg2 : arg1 + arg2*2
# print(Bharath)  # it will give the memory location because you have not a passed any inputs
# # #
# # # # calling function
# print("Value of total : ", Bharath(10, 20))
# print("Value of total : ", Bharath( 20, 30 ))

# c = lambda a, b: a**b
# # # # print(c)  # it will give the memory location because you have not passed any inputs
# #
# # calling function
# print(c(2,3))
# print(c(2,6))



# 2. Map Function
# =============

"""
map() :
map() will apply the function to every item of iterable and 
return a list of the results.
(or)
Map means Apply same function to each element of a sequence
Map returns the modified list.

Syntax :
map(function, iterable, ...)
"""
# # Ex : Create a list of squares for the first 5 numbers

# numbers = range(1,6)
# # squares = map(lambda x: x*x, numbers)
# squares = list(map(lambda x: x**x, numbers))
# # #
# print(squares)


# Note:- Need not necessarily use a lambda function print(list(map(square, iterable)))

# Filter Function:
# ================

""""
3. filter() :
The function filter(function, iterable) offers an elegant way to filter out all the elements of a list, 
for which the function function returns True. 
(or)
Filter items out of a sequence
returns filtered list
"""
# Ex: Print only the even numbers from 20 to 40
#
# def is_even(x):
#     if (x % 2 == 0):
#         return x
#
# numbers = range(20, 40)
# x = filter(is_even, numbers)
# x = list(filter(is_even, numbers))
# print(x)



# O / P: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

""" reduce()
Applies same operation to items of  a sequence
Uses result of operation as  a first parameter of next operation
returns an item, not a list"""
# from functools import reduce
#
# N = [5,4,2,3]
# multi = (reduce(lambda x,y:x*y,N))
# print(multi)



"""zip() function- it will take multiple lists say list1, list2, etc and transform them into a single list of tuples by taking the corresponding elements of the lists that are passed as parameters."""


# zip always creates the tuple in the order of iterables from left to right.
#  list_a will always be before list_b in the output tuples

# execute the below code in 2.7.x version it will give list of tuples.

# list_a = [1, 2, 3, 4, 5,8]
# list_b = ['a', 'b', 'c', 'd', 'e', 'f']
# # # # # # #
# zipped_list = zip(list_a, list_b)   # execute only in python 2.7.x version
# #print(zipped_list)
# print(list(zipped_list))


#

# In Python3, zip methods returns a zip object instead of a list. This zip object is an iterator.
# Iterators are lazily evaluated.
# Iterators returns only element at a time. len function cannot be used with iterators. We can loop over the zip object
#  or the iterator to get the actual list
# list_a = [1, 2, 3, 4, 5]
# list_b = ['a', 'b', 'c', 'd', 'e']
# #
# zipped_list = zip(list_a, list_b)
# # #
# N = list(zipped_list) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# print(N)
# B = list(zipped_list) # Output []... Output is empty list because by the above statement zip got exhausted.
# print(B)
#
#
# # zip with more than 2 lists

# list1 = ['A', 'B', 'C']
# list2 = [10, 20, 30,40]
# list3 = ["Narendra", "Surendra", "Aruna"]
# x = list(zip(list1, list2,list3))
# print(x)  # results in a list of tuples say [('A', 10, 'Narendra'), ('B', 20, 'Surendra'), ('C', 30, 'Aruna')]
# # #
# # #
# # # # # """whenever the given lists are of different lengths, zip stops generating tuples when the first list ends"""
# A0 = dict(zip(('a','b','c','d','e','f'),(1,2,3,4,5)))
# print(A0)
# #
# # Unzip a list of tuples
#
# # To unzip a list of tuples we zip(*listP_of_tuples). Unzip creates separate list.
# #
# zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# x, y = zip(*zipper_list)
# print(x)  # (1, 2, 3)
# print(y)  # ('a', 'b', 'c')

# For loop on zip concept
# Python program that uses zip on list
#
# items1 = ["blue", "red", "green", "white"]
# items2 = ["sky", "sunset", "lawn", "pillow"]
# # print(list(zip(items1, items2)))
# # Zip the two lists and access pairs together.
# for x, y in zip(items1, items2):
#     print(x, "==>",y)


# enumerate concept with zip
# Here is how to iterate over two lists and their indices using enumerate together with zip:
# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
# #
# for i, (a, b) in enumerate(zip(alist, blist)):
#     print(i, a, b)


#####**********    Practice Programs    *******####
# """Sorting a List of Tuples using Lambda"""
# list1 = [('eggs', 5.25), ('honey', 9.70), ('carrots', 1.10), ('peaches', 2.45)]
# list1.sort(key = lambda x: x[1])
# print(list1)
# # ans:[('carrots', 1.1), ('peaches', 2.45), ('eggs', 5.25), ('honey', 9.7)]

"""Sorting a List of Dictionaries using Lambda"""
# import pprint as pp
# list1 = [{'make':'Ford', 'model':'Focus', 'year':2013}, {'make':'Tesla', 'model':'X', 'year':1999}, {'make':'Mercedes', 'model':'C350E', 'year':2008}]
# list2 = sorted(list1, key = lambda x: x['year'])
# pp.pprint(list2)
#
# # Ans : [{'make': 'Tesla', 'model': 'X', 'year': 1999},
# #  {'make': 'Mercedes', 'model': 'C350E', 'year': 2008},
# #  {'make': 'Ford', 'model': 'Focus', 'year': 2013}]

# Ex : Find the cube of a given number

# cube = lambda x : x**3
# print(cube(2))
# print(cube(4))
# like lambda we can reuse lambda function so many time

# def divide(x, y):
#    try:
#       result = x / y
#    except ZeroDivisionError:
#        print("division by zero!")
#    else:
#        print("result is", result)
#    finally:
#        print("executing finally clause")
# divide(4,2)
#
# def divide(a,b):
#     try:
#         operation=a / b
#     except ZeroDivisionError:
#         print("Divison by Zero!")
#     else:
#         print("result is:", operation)
#     finally:
#         print("execution  finally clause" )
# divide(10,2)
#
#
# def divide(n,m):
#     try:
#         r=n/m
#     except ZeroDivisionError:
#         print("Division by Zero!")
#     else:
#         print("result is:",r)
#     finally:
#         print("execution Finally clause")
# divide(5,0)
# def sub(x,y):
#     try:
#         s=x-y
#         c=x/y
#         z=x*y
#     except ZeroDivisionError:
#         print("Division by zero")
#     else:
#         print("answer:",s,c,z)
#     finally:
#         print("execution finally caluse")
# sub(5,5)

