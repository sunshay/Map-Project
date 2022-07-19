# list of tupple


c = [ ('sun', 38, 4 ),
    ('doussey', 36, 2 ),
    ('herve', 35, 4 ),
    ('king', 32, 3 ),
    ('dick', 28, 2  ), 
    ('santa', 23, 1 )  
]

print(type(c))
from operator import itemgetter

k = itemgetter(1) #locate first index of tuple
print(map(k,c)) # print all first index of all tuple  

d = ('mum', 60, 5)
c.append(d)
print(c)