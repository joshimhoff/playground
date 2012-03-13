# a decorator that adds static-typing to python function arguments
# so evil...

# TODO: work with methods

def static_typing(*args, **kwargs):
    def my_decorator(func):
        # saved for later
        orderedTypes = args # list of types
        namedTypes = kwargs # dict of types
        def wrapped(*args, **kwargs):
            # check types before function call
            for i, each in enumerate(args):
                assert type(each) == orderedTypes[i]
            for k, v in kwargs.iteritems():
                assert type(v) == namedTypes[k]
            return func(*args, **kwargs)
        return wrapped
    return my_decorator

if __name__ == "__main__":
    # testing
    @static_typing(str, int)
    def test(dog, number):
        print dog
        print number

    # this should run
    test("dog", 5)
    # this should fail
    test(5.0, 6.0)

    # testing kwargs
    @static_typing(dog=str, number=int)
    def test(dog, number):
        print dog
        print number

    # this should run
    test(dog="golden", number=5)
    # this should fail
    test(dog=5.0, number="cat")
