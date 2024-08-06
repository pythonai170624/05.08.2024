
info: list[any] = [["name", "oren"], ["age", 31] ,[ "height", 1.98]]

info_dict: dict = {"name": "oren", "age": 31, "height": 1.98, "smoker": False, "brothers_age": [18, 20],\
             "address": {"city": "tel-aviv", "street": "ben-yehuda", "number": 12}}
#  data = {"33526127": {} }
print(info_dict)
print('get(name) =', info_dict.get("name"))

print(list(info_dict.values()))
print(list(info_dict.keys()))
print(list(info_dict.items()))
info_dict.get("address").get("street")
# targil1:
# create info_dict: name, age, height, smoker, address_dict
# input a key from the user
# print the dict value of this key using get

for k, v in info_dict.items():
    print(f"[{k}]: {v}, ", end=" ")

print()
for k in info_dict.keys():
    print(f"[{k}]: {info_dict.get(k)}, ", end=" ")
print()
for v in info_dict.values():
    print(f"{[key for key, val in info_dict.items() if val == v]}: {v}, ", end=" ")
print()
# for v in info_dict.values():
#     print(f"{[key for key, val in info_dict.items() if val == v]}: {v}, ", end=" ")
# print()

for item in info_dict.items():
    print(f"[{item[0]}]: {item[1]} , ", end=" ")
print()

info_dict.clear()
print('clear', info_dict)

info_dict = {"name": "oren", "age": 31, "height": 1.98, "smoker": False, "brothers_age": [18, 20],\
             "address": {"city": "tel-aviv", "street": "ben-yehuda", "number": 12}}

info_copy = info_dict.copy()
print('copy', info_copy)

print('from keys 1', dict.fromkeys(['name', 'smoker'], None))
print('from keys 2', dict.fromkeys(info_dict.keys(), None))

print('get name', info_dict.get('name'))
print('get weight', info_dict.get('weight', 0))

print('pop name', info_dict.pop('name'))
print('after pop name', info_dict)

print('pop item', info_dict.popitem())  # remove last item
print('after pop item', info_dict)

info_dict.update({"name": "danny", "age": 18})
print('after update', info_dict)
info_dict['name'] = 'moshe'  # [key]
print('after update', info_dict)
del info_dict['name']
print('after delete', info_dict)
try:
    del info_dict['name']
except:
    print('could not delete. does it exist?')

dict_books = dict([[1, "1984"], [3, "Harry potter"], [5, "Game of thrones"]])
dict_books = dict([(1, "1984"), (3, "Harry potter"), (5, "Game of thrones")])
print('len', len(dict_books))
print('from dict()', dict_books)
print('str', str(dict_books))
db_dict: dict = {True: {"name": "shalom", "age": 20}, 2: {}}
print(db_dict)
def add_two(x, y):
    return x + y
oper_dict0: dict= {"+": add_two}
oper_dict0.get("+")(1, 3)
#oper_dict0["+"]
#add_two(1, 3)
oper_dict: dict= {"+": lambda x,y: x + y} # add - * / // **
# input 2 numbers from the user
# input an operation + - * /
# get the value by using the operation as key
# execute the operation using the dictionary
print(oper_dict)
print(oper_dict["+"](1, 3))

oper_dict: dict= {"+": lambda x,y: x + y, "-": lambda x,y:x - y,\
                  "*": lambda x,y: x * y, "/": lambda x,y:x / y}
def mul(x, y):
    return x * y
x: int = int(input("enter x: "))
y: int = int(input("enter y: "))
oper: str = input("enter oper: ")  # + - * /
result = oper_dict.get(oper)(x, y)

print(f"{x} {oper} {y} = {result}")
for k in oper_dict.keys():
    result = oper_dict.get(k)(x, y)
    print(f"{x} {k} {y} = {result}")


