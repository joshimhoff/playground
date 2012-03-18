# REAL LAMBDAS in Python -- clearly a hack and a half
# can use to make ANONYMOUS FUNCTIONS -- with filter() for example

def ultimateLambda(arguments, code):    
    code = "def function(" + arguments + "):" + code
    exec code in locals(), globals()
    return function

if __name__ == "__main__":
    # basic usage -- real lambdas
    f = ultimateLambda("x, y", "return x+y")
    print f(2, 3)

    # more than just statements -- this is actually pretty cool
    f = ultimateLambda("array", "\n\tsum = 0\n\tfor elem in array:\n\t\tsum += elem\n\treturn sum")
    print f([1,2,3])

    # anonymous function -- function never saved in memory!
    print ultimateLambda("x, y", "return x*y")(3, 3)

    # real world usage -- with filter()
    array = [1,2,3,4,5]
    new = filter(ultimateLambda("s", "\n\tif s<4: return True\n\telse: return False"), array)
    print new
