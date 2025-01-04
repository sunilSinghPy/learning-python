def calculator():                       #1.
    print("1. For Addition")
    print("2. For Substraction")
    print("3. For Multiplication")
    print("4 For division")
    print("'q' to quit")

    def check_value(var):
        if var.isnumeric():
            return int(var)
        else:
            return False
    def get_input():
        val = input('Please enter any number: ')
        return int(val)

    def get_value(opration):
        var1 = get_input()
        var2 = get_input()
        if(opration == 1):
            return var1+var2
        elif(opration == 2):
            return var1-var2
        elif(opration== 3):
            return var1 * var2
        elif(opration == 4):
            return var1/var2
        else:
            return "error !"

    choice = ''
    while(choice!='q'):
        choice = input("Enter Your Choice: ")
        if(choice.isnumeric()):
           if(int(choice)==1):
               print(get_value(1))
               print("========================")
           elif (int(choice)==2):
               print(get_value(2))
               print("========================")

           elif (int(choice)==3):
               print(get_value(3))
               print("========================")

           elif (int(choice)==4):
               print(get_value(4))
               print("========================")

           else:
               print("Must enter Number Between 1 to 4")


        else:
            if(choice=='q'):
                print("Happy to help YOu. Thank YOu!")
                print("========================")
                break
            print("Not A Number! ")
def factorial():
    num = int(input("Enter a Number: "))

    fact = 0

    while (num != 1):
        if fact == 0:
            fact = fact + num
        else:
            fact = fact * num
        num = num - 1
    print(fact)
def odd_even():
    # input num
    # if num%2 = 0 even else odd
    num = int(input("Enter a Number: "))

    if (num % 2) == 0:
        print('Even')
    else:
        print("odd")
def greter_num():
    # num1 , num2
    # if num1> num2

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    if num1 > num2:
        print(f'greater number is {num1}')
    else:
        print(f'greater number is {num2}')
def natural_num():
    # natural number 1,2,3,4,5.........n

    num = int(input("Enter any number: "))

    for i in range(1, num + 1):
        print(i)
def ract_area():
    # Area of ractangle = l*b

    l = int(input("Enter leangth of rectangle: "))
    b = int(input("Enter width of rectangle: "))

    print(f'area of rectangle is {l * b}')
def squar_area():
    # Area of square = l*l

    l = int(input("Enter leangth of rectangle: "))
    print(f'area of rectangle is {l ** 2}')
def circle_area():
    # Area of circle = 2*3.14*r**2

    r = float(input("Enter radius of circle: "))
    print(f'area of circle is {2 * 3.14 * r ** 2}')
def triangel_area():
    # Area of triangel = (s*(s-a)*(s-b)*(s-c))**0.5

    a = int(input("enter first side: "))
    b = int(input("Enter Second side: "))
    c = int(input("Enter Third side: "))

    s = a + b + c / 2
    print(f'area of triangle is {(s * (s - a) * (s - b) * (s - c)) ** 0.5}')

print(''' 
    1. for calculator
    2. for Factorial
    3. for Odd/Even 
    4. for largest Number
    5. for natural Number Print
    6. for Area of rectangle
    7. for Area of square
    8. for Area of circle
    9. for Area of triangle
    10. for palindrom
    11. for Armstrong number 
    12. for reverse of number
     ***********************      
        ''')

