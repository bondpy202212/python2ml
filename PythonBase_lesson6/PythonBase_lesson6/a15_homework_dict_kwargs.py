
my_dict = {'first'  : 0.1,
           'second' : 0.2,
           'third'  : 0.3,
           'fourth' : 0.4,
           'fiveth' : 0.5
           }
#print(my_dict)

def function(**kwargs):
    #print(kwargs)
    for name, value in kwargs.items():
        #print(name)
        print(" '" + name + "' has value - ", value)

    
#function(one=1)
function(one=1, two=2, three=3)

#function(iter(my_dict))

#for name1, value in my_dict.items():
#    #print(name1)
#    #name1 = (name1)
#    function(name1 = value)

