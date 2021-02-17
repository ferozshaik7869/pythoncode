#import module file as md1 or as your wish module as md2 as md1 and md2 is another neme in simple way
#Refer another simple name inside of module or file which you have named
import module as md1
print(md1.add(7,4))
print(md1.sub(10,5))
print(md1.div(10,2))

import module as md2
print(md2.floordiv(10,2))

import module as sha
print(sha.mul(5,2))

from module import add,sub,mul,div# way2 to call function from module file
print(add(7,4))
print(mul(8,5))

from math import factorial,sqrt
print(factorial(30))
print(sqrt(30))


