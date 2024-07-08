# append()
# Append is used to add an element to the last index of the list

a = [1, 2, 3, 4, 5]
a.append(6)
print(a)

# Output - [1,2,3,4,5,6]


# clear()
# Removes all the elements from the list

b = [1, 2, 3, 4, 5, 6]
b.clear()
print(b)

# copy()
# Creates a copy of the list

c = [1, 2, 3, 4, 5, 6, 7]
x1 = c.copy()
print(x1)

# count()
# Returns the number of elements with a specified value.

d = [1, 2, 3, 4, 5, 6, 6]
x2 = d.count(6)
print(x2)

# index()
# Returns the index value of a particular element.

e = [1, 2, 3, 4, 5, 6]
x3 = e.index(1)
print(x3)

# insert()
# It is used to insert a value at a defined index inside the list.

list1 = [1, 2, 3, 4, 5, 6, 7]
list1.insert(2, 33)  # Here 2 is the index and 33 is the data item inserted
print(list1)

# pop()
# It is used to remove the last data item from the list.

f = [1, 2, 3, 4, 5, 6, 7]
f.pop()
print(f)

# remove()
# It is used to remove a particular item from a list.

g = [1, 2, 3, 4, 5, 6, 7]
g.remove(2)
print(g)

# reverse()
# It is used to reverse a list.

h = [1, 2, 3, 4, 5, 6, 7]
h.reverse()
print(h)

# sort()
# It is used to sort a particular list.

i = [122, 4, 5, 6, 77, 888, 9, 0]
i.sort()
print(i)
