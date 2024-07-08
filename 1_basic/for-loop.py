# for statement in python is used to iterate or repeat a set of statements or lists or strings
# or any sequence.
# In python, the for loop works better than the c language as it does not iterate over any
# numeric conditions.
# You can apply for loop in python over the list, string, tuple, dictionary, etc.

# example -1

name_list = ["Mradul", "Manal", "Hardik", "Sachin", "Gautam"]

for i in name_list:
    print(i, end=" ")

#example - for looping over a dictionary

#Created a dictionary
users = {'Mradul': 'active', 'Manal': 'inactive', 'Hardik': 'active'}

#Added for loop statement
for user, status in users.items(): #Here user is key and status is value
    if status == 'inactive':
        print(f"{user} is not a active user")

#example3:

# If you want to iterate the loop over a sequence of numbers between a range then
# the range function is used inside for loop.

for i in range(5):
    print(i)
print("****************************************")
for i in range(2,5):
    print(i)
print("****************************************")
for i in range(2,20,2):
    print(i)
print("****************************************")
for i in range(-2,-20,-5):
    print(i)

