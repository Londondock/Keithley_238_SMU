# globals.py

var1 = 0
var2 = 1

def function1():
    var1 = 1
    var2 = 2
    
    print var1, var2

def function2():
    global var1, var2
    
    print var1, var2

    var1 = 3
    var2 = 4

    print var1, var2