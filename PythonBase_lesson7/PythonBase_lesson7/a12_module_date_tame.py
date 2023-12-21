
import datetime

now = datetime.datetime.now()
print(now)
print(datetime.datetime.now() - now)
print()

some_day = datetime.datetime(year = 2005, month =5, day = 18, hour = 0, minute = 23, second = 18)
print(some_day)
print()

some_day += datetime.timedelta(days = 2, hours = 3)
print(some_day)
print()

some_day -= datetime.timedelta(hours=4)
print(some_day)
print()

print(some_day.strftime('%A. %d.%m.%Y'))
print()




#now2 = datetime.datetime.now()
#x =[]
#for i in range(10000):
#    #print(i)
#    x.append(i ** 5)

#now3 = datetime.datetime.now() 
#print(now3 - now2)
##print(x)