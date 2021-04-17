def swap(x,y):
    """(float,float)-> str
    
    Return the swapped values of two given values
    by creating a temporary variable.
    
    >>> swap(6.5,7.3) #6.5 as x, 7,3 as y
    The value of x after swapping is 7.3.
    The value of y after swapping is 6.5.
     """
    z=x
    x=y
    y=z
    print("The value of x after swapping is {}".format(x))
    print("The value of y after swapping is {}".format(y))
    
x=float(input("Please enter x: "))
y=float(input("Please enter y: "))
swap(x,y)
