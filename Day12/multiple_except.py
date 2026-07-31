try:
    num1 = int(input("enter first number:"))
    num2 = int(input("Enter second number:"))
    
    result = num1/num2
    
    print("result:",result)

except ValueError:
    print("please enter only numbers!")

except ZeroDivisionError:
    print("Cannot divide by Zero!")