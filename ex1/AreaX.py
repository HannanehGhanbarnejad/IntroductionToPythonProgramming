def AreaX(a, b, c, d, e):
    """(float, float, float, float, float)-> str


   Return the area of the triangle or the quadrilateral. If one of the fist four given
   values was equal to zero,the function calculates the area of the triangle.
   If not, the function calculates the area of the quadrilateral. In both states the
   funntion checks the triangle inequality theorem in order to find out if the triangle
   or the quadrilateral can be made withe the given values or not.


   >>>AreaX(0, 6, 6, 9, 12)
   'The area of the triangle: 17.858821349685986'
   >>>AreaX(20, 2, 0, 18, 9)
   'The triangle cannot be made.'
     >>>Area(17, 15, 20, 13, 12)
   'The area of the quadrilateral: 162.6558352068144'
   >>>Area (6, 4, 9, 14, 12)
   'The quadrilateral cannot be made.'
   
   """
    if ((a+b)>c and (a+c)>b and (b+c)>a) and (d==0):
        S=(a+b+c)/2
        triangleArea=(S*(S-a)*(S-b)*(S-c))**0.5
        print("The area of the triangle: {}".format(triangleArea))
        
    elif ((d+b)>c and (d+c)>b and (b+c)>d) and (a==0):
        S=(b+d+c)/2
        triangleArea=(S*(S-b)*(S-d)*(S-c))**0.5
        print("The area of the triangle: {}".format(triangleArea))

    elif((d+b)>a and (d+a)>b and (b+a)>d) and (c==0):
         S=(b+d+a)/2
         triangleArea=(S*(S-b)*(S-d)*(S-a))**0.5
         print("The area of the triangle: {}".format(triangleArea))

    elif((d+c)>a and (d+a)>c and (c+a)>d) and (b==0):
         S=(c+d+a)/2
         triangleArea=(S*(S-c)*(S-d)*(S-a))**0.5
         print("The area of the triangle: {}".format(triangleArea))


    elif(((a+b)>c and (a+c)>b and (b+c)>a)!=True) and ((d==0)==True):
         print("The triangle cannot be made.")
         
    elif(((d+b)>c and (d+c)>b and (b+c)>d)!=True) and ((a==0)==True):
         print("The triangle cannot be made.")
         
    elif(((a+b)>d and (a+d)>b and (b+d)>a)!=True) and ((c==0)==True):
         print("The triangle cannot be made.")
         
    elif(((a+d)>c and (a+c)>d and (d+c)>a)!=True) and ((b==0)==True):
         print("The triangle cannot be made.")
       
    elif((a+b)>e and (a+e)>b and (b+e)>a) and((c+d)>e and (c+e)>d and (d+e)>c) :
        S1=(a+b+e)/2
        A1=(S1*(S1-a)*(S1-b)*(S1-e))**0.5
        S2=(e+c+d)/2
        A2=(S2*(S2-e)*(S2-c)*(S2-d))**0.5
        quadrilateralArea= A1+A2
        print("The area of the quadrilateral: {}".format(quadrilateralArea))
        
    elif((a+b)>e and (a+e)>b and (b+e)>a) and((a+c)>e and (a+e)>c and (c+e)>a) :
        S1=(a+c+e)/2
        A1=(S1*(S1-a)*(S1-b)*(S1-e))**0.5
        S2=(a+b+e)/2
        A2=(S2*(S2-a)*(S2-b)*(S2-e))**0.5
        quadrilateralArea= A1+A2
        print("The area of the quadrilateral: {}".format(quadrilateralArea))
    else:
        print("The quadrilateral cannot be made.") 

a=float(input("Enter side A: "))
b=float(input("Enter side B: "))
c=float(input("Enter side C: "))
d=float(input("Enter side D: "))
e=float(input("Enter side E: "))

AreaX(a, b, c, d, e)

