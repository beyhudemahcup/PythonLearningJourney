def cube():
    # known practice
    """
    result = []

    for i in range(5):
        result.append(i ** 3)
    return result
    """

    #  best practice for enormous data if we don't need to use them for the second time
    for i in range(12):
        yield i ** 3  # it will dissappear after execution


generator = cube()

iterator = iter(generator)

for i in iterator:
    print(i)

#comprehensive
#list version of cube data
my_list = [i ** 3 for i in range(5)]
print(my_list)
#generator version of cube data
my_generator = (i ** 3 for i in range(5))

for i in my_generator:
    print(i)

