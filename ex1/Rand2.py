a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
def Rand2(a,b):
    """ (int,int)-> int

    Return a random even number within a specific range between two given values
    including the values themselves.

    >>> Rand2(30,127)
    58
    """
    
    import random
    for i in range(a,b+1):
        i=random.randint(a,b)
        if i%2 !=0:
            continue
        print(i)
        break
Rand2(a,b)

