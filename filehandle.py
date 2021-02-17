#file handling
#r is raw data
#creating the file in any drive ,we want to make changes or read we have go through the following procedure
#variable name=open("path","mode")
# path is location of the file and mode  write,read,append
#w=write the values in the file(file is exits---->write the value else create& write)
#r=read the values(file must be present)
#a=append content
#w+,r+
# files(.txt....)
# Binary files(images,audios,videos)
# writing values in the file
#
f=open(r"D:\anto.doc","w")
f.write("hello  imthiyaz ali")
f=open(r"D:\imthiyaz.doc","r")
f=open(r"D:\imthiyaz.doc","a+")
#print(f.append())
print(f.read())# we can read the content  in the file by running this code
result=f.read()
print(result)
f.close()
# f.a("hello feroz")
f.close()
#

#
# f=open(r"D:\ferozpythonclass.doc","r")
# result=f.read()# another way of printing values in pycham
# print(result)
#
# f=open(r"D:\feroz.doc","w")
# f.write("HELLO HERO OF PYTHON i want to be a good coding programmer")
# f.close()
#
# f=open(r"D:\function.doc","r")
# print(f.read())
# f.close()

# f=open(r"D:\feroz.doc","r")
# for i in range(10):
#     print(f.tell())# it tells the  start index of the value
#     print(f.readline())# after reading the value
#     print(f.tell())# it tells the last index of the value

f.close()

# #mode are as follows
# f=open(r"d:\pythonsample.txt","w")
# f.write("my kids are  my Heros")
# f.close()

#same as above with write mode "w"
# if we want to write the value in the same file it will overwrite
# f=open(r"d:\pythonsample.txt","w")
# f.write("hello world of adventures")
# f.close()

# for that we have another mode called append mode "a".
# its just append means add value to the Existing file
# f=open(r"d:\pythonsample.txt","a")
# print(f.tell())#find the cursor in which index position
# f.seek(0)#move position cursor to start position
# # print(f.read())
# f.write("\n i will reach my goal")#write i as a method in the function# \n denotes new line.
# f.seek(40)
# print(f.tell())
# f.close()# if you intize a file to open best practice to close

# below one to create anew file in the pycham itself
# f=open(r"d:\shareef.txt","r+")# in the mode first read the value in the file and
# # then write any content in the file
# print(f.read())#read method
# f.writelines(['feroz','feroz@gmail.com','python'])
# f.writelines(['shareef','shareef@gmail.com','seleium'])
# f.close()
# f=open("d:\kursheed.txt",'a+')#write the value else create& write)
# f.writelines(['\nyaseen','yaseen@gmail.com','yaseen_salarydetails'])#first i created the file by write mode
# # after append
# print(f.tell())
# print(f.read())
# print(f.seek(0))
# print(f.seek(2000))
# print(f.tell())
# f.close()
f=open(r"d:\kursheed.html","w+",newline="")
f.writelines(["kursheed","Assissote professer","institue:chalapathi"])
f=open(r"d:\kursheed.html","a+",newline="")
f.writelines(["\nferoz:husband of kursheed"])
f.close()

