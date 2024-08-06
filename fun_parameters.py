x: int = 1
print('before func: (glbal x)', x)


# ----- function -------
def add1(x: int) -> None:
    x = x + 1
    print('inside add1 ----> ', x)


# -----------------------

add1(x)  # by value
print('after func: (global x)', x)

list_int: list[int] = [1, 2, 3]
print('\nbefore func --> ', list_int)  # [1, 2, 3]


# ----- function -------
def add1_list(alist: list[int]) -> None:
    alist.append(100)

add1_list(list_int)
# -----------------------

add1_list(list_int)
print('after func -->', list_int)  # [1, 2, 3, 100]


# ----- function -------
def clear_list(blist: list[int]) -> None:
    # mutable
    blist = [1]
    # blist.clear()
    print('inside clear #300', blist)


# -----------------------

print('\nbefore clear #100 -->', list_int)  # [1, 2, 3, 100]
clear_list(list_int)
print('after clear #100 ---> ', list_int)  # [1, 2, 3, 100]


# ----- function -------
def add1_str(str1: str) -> None:
    # str == immutable
    # str1 == #55
    str1 = str1 + "!"
    print('inside add1_str: ', str1)


# -----------------------

my_str: str = "hello"
print()
print('before -->', my_str)  # "hello" # 55
add1_str(my_str)
print('after add1_str func --> ', my_str)  # "hello"


def add1(list1: list[int]) -> None:
    list1.append(100)


def add1_global() -> None:
    # do not need global
    global nums
    nums.append(100)


nums: list[int] = [1, 2, 3]

x = 10


# BAD
def add1_change() -> None:
    global x
    x = x + 1


# GOOD
def add1_change(x: int) -> int:
    x = x + 1
    return x


x = add1_change(x)
print(x)

y: int = 20


def add2(x: int, y: int) -> [int, int]:
    x = x + 2
    y = y + 2
    return x, y
print('before', x, y)
x, y = add2(x, y)
print('after', x, y)
