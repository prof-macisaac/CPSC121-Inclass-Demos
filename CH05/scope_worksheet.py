##### Example 1
x = 10
def f():
    x = 5
    print(x)
f()
print(x)

##### Example 2
msg = "hi"
def g():
    print(msg)
g()

##### Example 3
def h():
    y = 42
    print(y)
h()
# print(y)

##### Example 4
n = 7
def add_one(n):
    n = n + 1
    print(n) # prints 8
add_one(n)
print(n) # prints 7

##### Example 5
value = 100
def set_local():
    value = 50
    print(value) # prints 50
set_local()
print(value) # prints 100

##### Example 6
count = 0
def inc():
    global count
    count = count + 1
inc()
inc()
print(count) # prints 2

##### Example 7
total = 0
def bad_add():
    total = total + 5 # error!
# bad_add()

##### Example 8
x = 2
def f():
    print(x) # prints 2
def g():
    x = 8
    f()
g()

##### Example 9
a = 3
def change():
    global a
    a = a + 10
change()
print(a) # prints 13

##### Example 10
x = 1
def outer():
    x = 99
    print(x) # prints 99
outer()
print(x) # prints 1

##### Example 11
x = -1

def change():
    global x
    x += 1

def main_1():
    x = 5
    change()
    print(x) # print 5

def main_2():
    global x
    x = 5
    change()
    print(x) # prints 6

main_1()
main_2()