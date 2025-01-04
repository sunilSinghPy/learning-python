# Area of triangel = (s*(s-a)*(s-b)*(s-c))**0.5

a = int(input("enter first side: "))
b = int(input("Enter Second side: "))
c = int(input("Enter Third side: "))

s = a+b+c/2
print(f'area of triangle is {(s*(s-a)*(s-b)*(s-c))**0.5}')