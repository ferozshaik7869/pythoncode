# create a csv file(comma seperated value)
# variable=open("path/name.csv","w")
# import csv# if package not available install it
#create and write csv
import csv
f=open("sample.csv","w",newline='')#it will create the file of csv in phycam itself
c=csv.writer(f)# store in another variable
c.writerow(['helo','heloo@yahoomail.com','hello_id'])#here no need  to  close in csv file
#
import csv
f=open("sample.csv","w",newline='')
s=csv.writer(f)
f=open("sample.csv","a",newline="")
s.writerow(['hello','python','programmer'])
s.writerow(['feroz','python programmer'])
s.writerows(["shareef","java programmer","yaseen"])
s.writerows(["hello hero"])
####################################################
import csv
f=open("feroz.csv","w",newline="")
v=csv.writer(f)
v.writerow(["python","seleium","tester","feroz"])
v.writerows((["hello python programmer"]))
#########################################################
import csv
f=open('employeefile.csv',"w",newline='')
c=csv.writer(f)
c.writerow(['johnsmith','accounting','November'])
c.writerow(['Erica meyers','IT','march'])
#############################################################

import csv
f=open("employeefile.csv",'r')
x=csv.reader(f)
result=csv.reader(f)
print(type(result))
print(f.tell())
print(f.seek(0))
print(list(result))
print(f.seek(1000))
######################################################
import csv
with open("employeefile.csv",'w+') as f:#way 2 create a file
    d=csv.writer(f)
    d.writerow(['feroz','feroz@gmail.com'])
    result=csv.reader(f)
    print(f.tell())
    print(f.seek(0))
    print(type(result))
with open("ferozshaikfile.csv","w")  as k:
    e=csv.writer(k)
    e.writerow(['kursheed','kursheed7869@gmail',"uni_id"])
    result=csv.reader(k)
    print(k.seek(0))
    print(k.tell())
#########################################
with open("feroz family.csv",'w') as d:
    d=csv.writer(d)
    d.writerow(["yaseen","yaseen@shareef.com"])
################################################
import csv
f=open("kursheed.csv",'w')
n=csv.writer(f)
n.writerow(['kursheed','kursheed@gmail.com','employeeid:2542'])
print(type(n))

import csv
f=open("yaseen.csv",'w')
x=csv.writer(f)
x.writerow(['yaseen','yaseen@gmail.com','employeeid:7866'])
print(x,type(x))

import csv
f=open("yaseenshareef.csv",'w')
s=csv.writer(f)
s.writerow(['yaseenhero','yaseen@yahoo.co.in','employee2:7855'])
print(s,type(s))

import csv
f=open("yaseenshareef.csv",'w')
s=csv.writer(f)
s.writerow(['hellojakir'])
print(s,type(s))


import csv

with open('employee_file2.csv', mode='w') as f:
    fieldname = ['emp_name', 'dept', 'birth_month']
    h = csv.DictWriter(f,fieldnames=['emp_name', 'dept', 'birth_month'])
    print(f.tell())

    h.writeheader()
    h.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    h.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

import csv
with open('employee_file3.csv',"w") as f:
    fieldnames=['employee_id','salary_details','adress']
    x=csv.DictWriter(f,fieldnames)
    x.writeheader()
    x.writerow({'employee_id':'12455','salary_details':'52000','adress':'chuttugunta'})


import csv
with open("employee_file3.csv","a") as f:
    fieldnames=['emp_list','emp_id','office location']
    d=csv.DictWriter(f,fieldnames)
    d.writeheader()
    d.writerow({'emp_id':'45211','emp_list':'feroz,\nkursheed','office location' :'bangalore'})

import  csv
with open("employee_file3.csv","a") as f:
    fieldnames=['emp_name']
    b=csv.DictWriter(f,fieldnames)
    b.writeheader()
    b.writerow({'emp_name':'shaik'})

# # way2 of creating a file
# with open("d:\kursheed.txt","r+") as f:# "w+" means first write mode and than raed mode
#     f.write("iam writing in the kursheed txt file")# it dispalyas in ide phycam as well write in th file
#     # which is in the path location
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())
#
# with open("d:\yaseen.txt","w+") as f:
#     f.writelines(["feroz","khan "])
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())

