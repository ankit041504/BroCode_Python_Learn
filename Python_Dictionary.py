dict1={"name": "mradul","age": 23,"city": "indore"}
print(dict1)

dict1 = {"name":"mradul","age":23,"city":"indore"}
print(dict1.keys())

dict1 = {"name":"mradul","age":23,"city":"indore"}
print(dict1.values())

# clear(): This method removes all items from the dictionary.

dict1 = {"name": "John", "age": 30}
dict1.clear()
print(dict1)  # Output: {}


# copy(): This method returns a shallow copy of the dictionary.

dict1 = {"name": "John", "age": 30}
dict2 = dict1.copy()
print(dict2)  # Output: {"name": "John", "age": 30}


# get(): This method returns the value of a specified key. If the key is not found,
# it returns a default value.

dict1 = {"name": "John", "age": 30}
print(dict1.get("name"))  # Output: "John"
print(dict1.get("gender", "Unknown"))  # Output: "Unknown"

#items(): This method returns a list of key-value pairs in the dictionary.

dict1 = {"name": "John", "age": 30}
print(dict1.items())  # Output: dict_items([('name', 'John'), ('age', 30)])


#pop(): This method removes and returns the value of a specified key.

dict1 = {"name": "John", "age": 30}
value = dict1.pop("age")
print(value)  # Output: 30
print(dict1)  # Output: {"name": "John"}

#popitem(): This method removes and returns the last inserted key-value pair from the dictionary.

dict1 = {"name": "John", "age": 30}
item = dict1.popitem()
print(item)  # Output: ('age', 30)
print(dict1)  # Output: {"name": "John"}

#setdefault(): This method returns the value of a specified key. If the key is not found,
# it inserts the key with a default value.

dict1 = {"name": "John", "age": 30}
value = dict1.setdefault("gender", "Male")
print(value)  # Output: "Male"
print(dict1)  # Output: {"name": "John", "age": 30, "gender": "Male"}

#update(): This method updates the dictionary with the key-value pairs from another dictionary.

dict1 = {"name": "John", "age": 30}
dict2 = {"gender": "Male", "city": "New York"}
dict1.update(dict2)
print(dict1)  # Output: {"name": "John", "age": 30, "gender": "Male", "city": "New York"}

