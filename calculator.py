import math

def add():
    num1 = int(input("Enter firsts number: "))
    num2 = int(input ("Enter second number: "))
    result = num1 + num2
    print(f"Answer is :  {result}")

def subtract():
    num3 = int(input("Enter first number: "))
    num4 =int(input("Enter second number: "))
    result2 = num3 - num4
    print(f"Answer is :  {result2}") 

def multiply():
    num5 = int(input("Enter first number: "))
    num6 = int(input("Enter second number: ")) 
    result3 = num5 * num6
    print(f"Answer is :  {result3}")  

def division():
    num7 = int(input("Enter first number: "))
    while True:
        num8 = int(input("Enter second number: "))  
        if num8 == 0:
            print("You cannot divide by zero")
        else:
            break
    result4 = num7 / num8    
    print(f"Answer is : {result4}")

def power():
    print("Exponential function")
    base = int(input("Enter base number: "))
    exponent = int(input("Enter exponent: "))
    result5 = math.pow(base, exponent)
    print(f"Result: {result5}")

def square_root():
    num9 = int(input("Enter number: "))
    result6 = math.sqrt(num9)
    print(f"Square root is : {result6}")

def percentage():
    num10 = int(input("Enter number : "))  
    while True:
        if num10 == 100:
            print("Cannot find percentage of 0")
        else:
            break
    result7 = num10 / 100
    print(f"Percentage is : {result7}%")

def main():
    print("WELCOME TO SANJAY'S CALCULATOR")
    print("Press respective keys to start")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.PERCENTILE SIDE")
    print("6.SQUARE ROOT")
    print("7.EXPONENTIAL")

    while True:
        # main()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add()
        if choice == 2:
            subtract()
        if choice == 3:
            multiply()
        if choice == 4:
            division()
        if choice == 5:
            percentage()
        if choice == 6:
            square_root()   
        if choice == 7:
            power() 
        else:
            break    
        

main()                            





    
     
    




    