# global
a=2
def changeA():
    a=3
    # print(a)
    return a
def changeG():
    global a
    a=5
b=changeA()
print(a)
print(b)

changeG()
print(a)