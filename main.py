def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,6,2,1,7,4,3))

def calculate(**kwargs):
    print(kwargs)

claculate(add=3, multiply=5)