def func1():
    """  (str)-> list

    The function recieves sentences as a string and turns
    it into words and returns the words as a list.

    >>>func1(Hello! My name is Hannaneh!)
    ['Hello!', 'My', 'name', 'is', 'Hannaneh!']

    """
    
    a=input("Please enter a string: ")
    b=a.split()
    print(b)

func1()
