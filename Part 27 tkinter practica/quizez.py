def foo(a, b=4, c=6): 
    print(a, b, c)
 
# foo(1)
#========================================#
def foo(a, b=4, c=6): 
    print(a, b, c)
 
# foo(4, 9)
#========================================#
def foo(a, b=4, c=6):
    print(a, b, c)
 
# foo(20, c=6)

#=========================================#

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
# bar(1, 2)
# 

#=========================================#

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
# bar(toast='nah', spam=4, eggs=2)
# 4, 2, nah, 0

#=========================================#

def test(*args):
    print(type(args))
 
# test(1,2,3,5) #arg = 1,2,3,5

#=========================================#

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64) # **kw = {'x': 10, 'y': 64}


