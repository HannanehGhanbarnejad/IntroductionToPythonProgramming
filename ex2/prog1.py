a=int(input("Please enter the first number:"))
b=int(input("Please enter the second number:"))

def prog1(a, b):
    """ (int, int)-> list

    Return all the even numbers between two given values.
    The function does not work when the first given value
    is bigger than the second one numerically .

    >>> prog2(23, 3) #23 as a, 3 as b
    No answer!
    The first number must be smaller than the second number.
    
    >>> prog2(56, 67) #56 as a, 67 as b
    The even numbers between 56 and 67 are: 
    [56, 58, 60, 62, 64, 66]
    
    """
    if a<b:
        print("The even numbers between", a, "and", b, "are: ") 
        L=[]
        for i in range(a, b+1):
            if i%2 == 0:
                L.append(i)
        print(L)
    else:
        print("No answer! \nThe first number must be smaller than the second number. ")

prog1(a, b)
