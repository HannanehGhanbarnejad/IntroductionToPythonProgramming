def equation2D(a,b,c):
    """ (float,float,float)-> str, float
    
    Return the roots of a quadratic equation by finding the Delta,
    using the given values as the numerical coefficients of the 
    equation.
    
    >>> root(1.0, 2.0, -15.0)
    The equation has two real roots.
    x1= 3.0
    x2= -5.0
    >>>root(1.0, -4.0, 4.0)
    The equation has one real root.
    x1=x2= 2.0 
    >>>root(2.0, 3.0, 4.0)
    The equation has no roots.
    """
    delta=b**2-4*a*c
    if delta<0:
       print("The equation has no roots.")
    elif delta==0:
        print("The equation has one real root.")
        print("x1=x2=", -b/(2.0*a))
    else:
        print("The equation has two real roots.")
        print("x1=",(-b+delta**0.5)/(2.0*a))
        print("x2=",(-b-delta**0.5)/(2.0*a))
a=float(input("Please enter a: "))
b=float(input("Please enter b: "))
c=float(input("Please enter c: "))
equation2D(a,b,c)

