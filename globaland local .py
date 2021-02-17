# **********************************************************
# global and local inilization
# temp = 10 	 # global-scope variable
#
# def func():
#       temp = 20   # local-scope variable
#       print(temp)
#
# print(temp) 	 # output => 10
# func() 		 # output => 20
# print(temp) 	 # output => 10

# *******************************
# This behaviour can be overriden using the global keyword inside the function, as shown in the following example:
# temp = 10 	 # global-scope variable

# def func():
#       global temp
#       temp = 20   # local-scope variable
#       print(temp)
#
# print(temp) 	 # output => 10
# func() 		 # output => 20
# print(temp) 	 # output => 20

# *******************************************
# same with example with string local and global
# a="feroz" #global variable
# def kursheed():
#     a="yaseen"# loacl variable
#     print(a)
# print(a)
# kursheed()
# print(a)
# print(a)


# a="feroz"
# def kursheed():
#     global a#accessing global variable inside function
#     a="shareef"
#     a="yaseen"
#     a="kursheed"# last varaible in the function ony executes
#     print(a)
# print(a)
# print(a)
# kursheed()
# print(a)


