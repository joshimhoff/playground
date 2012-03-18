# REAL LAMBDAS in Python -- clearly a hack and a half
# can use to make ANONYMOUS FUNCTIONS -- with filter() for example

# TODO: currently, ultimateLambda can't return values, so pretty useless

def ultimateLambda(code, unnamedArgs=[]):    
    # a closure!
    def function(*args, **kwargs):
        # args
        for i, arg in enumerate(unnamedArgs):
            locals()[arg] = args[i]
        # kwargs
        for k, v in kwargs.iteritems():
            locals()[k] = v
        exec code in locals(), globals()
    return function

if __name__ == "__main__":
    # basic usage -- real lambdas with more than statements
    f = ultimateLambda("for i in range(10):\n print i")
    f()

    # lambda with arguments
    f = ultimateLambda("print arg1\nprint arg2", ["arg1", "arg2"])
    f("cat", 4)

    # lambda with named arguments
    f = ultimateLambda("print arg1\nprint arg2")
    f(arg1 = "dog", arg2 = 3)

    # anonymous function! -- function never saved in memory
    ultimateLambda("print bird", ["bird"])(5.0)
