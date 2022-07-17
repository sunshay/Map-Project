# checking a list for some condition ( using iterables )
#for loop 
 # if condition
#output expression

from hashlib import new


new_list = []
for i in range(1,10):
    if i % 2 != 0:
     new_list.append(i**2)
print(new_list)

# #List comprehension [expression for loop if conditional]
new_lists = [ i**2 for i in range(1,10) if i%2 == 0]


#List comprehension [expression for loop if conditional]
new_lists = [x**2 for x in range(1, 11) if x%2 == 0 ]
print(new_lists)