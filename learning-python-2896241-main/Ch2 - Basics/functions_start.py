#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function


# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value


# TODO: function with default value for an argument


# TODO: function with variable number of arguments
def multi_add(test1, *args):
    result = 0
    print(test1)
    for x in args:
        result = result + x
        print(result)
    return result

#print(func2(12, 13))

print(multi_add("a",4,5,3))