def multiple_args(a,b,c,d):
    print ("Calling multiple optional arguments")
    if a:
        print (a)
    elif b:
        print (b)
    elif c:
        print (c)
    elif d:
        print (d)   
    
def hello(x):
    print ("Calling hello world through different concatenations")
    print ("Hello",x)
    print ("Hello" + x)
    print ("Hello" + x*3)
    
def iter():
    print ("Calling iterator functions")
    str = "Hi this is Radio 98.0"
    for i in str:
        print (i*3)
        
def strops():
    print("Calling string operations")
    temp = "a"
    temp = temp * 3
    return temp, temp*4

def fibo():
    print ("Calling fibonacci function")
    a,b = 0,1
    while b < 10:
        print (b)
        a,b = b , a+b
        
def f(x):
    return {
        'a': a,
        'b': b,
    }[x]

fibo()
str_arr = [0] *2
str_arr = strops()
print (str_arr)
iter()
hello("world")
multiple_args(a="3232",d="3332")

