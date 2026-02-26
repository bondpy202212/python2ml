# 1) ----------
#import a13_homework_primenumbers1
#count = int(input("enter numbet for print simple numbers: "))
#count = 10
#for n in a13_homework_primenumbers1.primes():
#    if n > count:
#        break
#    print(n)


## 2) ----------
#import a13_homework_primenumbers1 as f_pr

#count = 10
#for n in f_pr.primes():
#    if n > count:
#        break
#    print(n)


## 3) ----------
#from a13_homework_primenumbers1 import primes 

#count = 10
#for n in primes():
#    if n > count:
#        break
#    print(n)


# 4) ----------
from a13_homework_primenumbers1 import primes as pr123

count = 10
for n in pr123():
    if n > count:
        break
    print(n)