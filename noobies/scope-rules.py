# Scope - what variables do I have access to?

a = 1  # a is  in global scope hence we can access it from anywhere however in functions we have to declare it global


def confusion():
    a = 5  # where a is locally scoped only inside this function we have access to a
    return a


print(a)
print(confusion())
