list1=[(12, 18), (20, 25)]

def func4(list1):
    """  (list)->list

    Return the simplest face and denominator of each
    fractions that are recieved as tuples in a list.
    The function receive a list of tuples. Each tuple
    has two elements that are the face and denominaor
    of a fraction.

    >>>func4(list1)
    [(2, 3), (4, 5)]
    
    """
    
    from math import gcd
    list2=[]
    for i in range(0, len(list1)):
    
        x=list1[i][0]
        y=list1[i][1]
        d=gcd(x, y)
        x= x // d
        y= y // d
        lis2=list2.append((x, y))
    print(list2)
    
func4(list1)

