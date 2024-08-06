
def foo():
    # 1
    # no global - read only.
    # do not need to declare
    print('foo read-only (not using global keyword)', x)

# 5 -- try to change read-only
#x = x + 1  # Error - must use global

def goo():
    # 2
    global x
    x = x + 1  # OK
    print('changed in goo', x)

def moo(x: int):
    # 3
    # global x  # Error because there is a local
    x = x + 1
    print('moo', x)

def hoo():
    # 4
    x: int = 12
    x = x + 2
    print('hoo', x)

def koo():
    # 6
    # print(x) # Error
    x: int = 1

def main():
    # print(y)  # Error
    # y: int = 1

    # global
    x: int = 1
    foo()
    goo()
    moo(10)
    hoo()
    print(x)

if __name__ == "__main__":
    main()
