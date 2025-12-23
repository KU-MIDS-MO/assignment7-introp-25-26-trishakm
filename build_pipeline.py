def build_pipeline(operation_names):
    
    def add(x):
        return x + 1

    def subtract(x):
        return x - 1

    def double(x):
        return x * 2

    def triple(x):
        return x * 3

    def square(x):
        return x ** 2

    operations = {
        "add": add,
        "subtract": subtract,
        "double": double,
        "triple": triple,
        "square": square
    }

    for name in operation_names:
        operations[name]

    def pipeline(value):
        result = value
        for name in operation_names:
            result = operations[name](result)
        return result

    return pipeline
    
    pass

#Write a function:

#build_pipeline(operation_names)


#where operation_names is a list of strings.

#The function must return a new function that applies a sequence of operations to a single input value,in the given order.

#Each string in operation_names represents an operation



#If an unknown operation name is encountered, an error must be raised.

#Calling the returned function should apply all operations sequentially and return the final result.