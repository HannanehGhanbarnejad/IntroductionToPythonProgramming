n=int(input("Please enter a number: "))

def prog3(n):
    """ (int)-> bool

    Return the result of checking whether the
    given integer value is prime or not.

    >>> prog3(4)
    False

    >>> prog3(17)
    True
    
    """
    
    if n==1:
        print(False)
    else:
        for i in range(2, n):
            if n % i == 0:
                print(False)
                break
    
            else:
                print(True)
                break

prog3(n)
