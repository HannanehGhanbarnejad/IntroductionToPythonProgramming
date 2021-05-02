a=int(input("Please enter the first number:"))
b=int(input("Please enter the second number:"))
def prog2(a, b):
    """ (int, int)-> list

    Return all the even numbers between two given values.
    The function works even if the first given value is
    bigger than the second one numerically .

    >>> prog2(23, 3) #23 as a, 3 as b
    [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    
    >>> prog2(56, 67) #56 as a, 67 as b 
    [56, 58, 60, 62, 64, 66]

     """
    if b>a:
        L=[]
        for i in range(a,b+1):
            if i%2 == 0:
                L.append(i)
        print(L)
    else:
        L1=[]
        for j in range(b,a+1):
             if j%2 == 0:
                 L1.append(j)
        print(L1)
        
prog2(a, b)

