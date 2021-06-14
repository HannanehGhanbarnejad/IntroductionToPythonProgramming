def func2():
    """  (str)-> float

    The function recieves a string value and turns
    it into a floating point number.

    >>>func2(12.48)
    12.48

    """
    a=input("Plrase enter a floating point number: ")
    numbers={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
    num=0
    char='.'
    if char in a:
        x=len(a)-1-a.find(char)
        for i in a:
            if i!='.':
                num=num*10 + numbers[i]
                num1= num/10**x
        print(num1)   
    else:
        print('The entered number must  be a floating point number!')


func2()




