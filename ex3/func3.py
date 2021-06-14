def func3():
    """  (str)-> int

    The function recieves a floating point number and
    turns it into an integer number.

    >>>func3(12.48)
    12
    
    """
    a=input("Plrase enter a floating point number: ")
    numbers={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    num=0
    char='.'
    if char in a:
        x=len(a)-a.find(char)
        a=a[:-x]
        for i in a:
            if i !='.':
                num=num*10 + numbers[i]
                
        print(num)   
    else:
        print(a)


func3()


