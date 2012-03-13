# the classic exercise -- write a program that reproduces its own source

x = """def foo(x=x, y=1):
    if y:
        foo("\"x = " + x+"\"", 0)
    print x
foo(x)"""

def foo(x=x, y=1):
    if y:
        foo("x = \"" + x+"\"", 0)
    print x

foo(x)
