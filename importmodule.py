import csv
f=open("imthiyaz.csv","w",newline='')
x=csv.writer(f)
print(f.seek(0))
x.writerow(["feroz","software employee"])
import csv
f=open("hello.csv","w",newline='')
y=csv.writer(f)
y.writerow(["imthiyaz","design Engineer"])
print(y)
import csv
f=open("imthiyaz.csv","r",newline='')
y=csv.reader(f)
print(f.seek(0))
print(f.tell())
print(x)