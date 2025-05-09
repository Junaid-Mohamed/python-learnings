username = "Junaid"

def func():
    username =  "Mohammed"
    print(username)

print(username)
func()

x = 90

def fun2():
    y = x + 10
    print(y)

fun2()

def fun3():
    global x
    x = 20

# fun3()
print(x)

"""
closures 
aka factory functions
"""
def f1():
    a = 17
    def f2():
        print(a)
    return f2

f1()()

# another ex

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

print(chaicoder(2)(4))