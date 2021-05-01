a=int(input("Please enter a number: "))

def prog4(a):
    """ (int)-> list

    Return all the divisors of the given integer value.
    
    >>> prog4(14)
    [1, 2, 7, 14]

    >>> prog4(61)
    [1, 61]

    """
    L=[]
    for i in range(1,a+1):
        if a%i ==0:
            L.append(i)
    print(L)

prog4(a)
