def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
def maximum3(num1, num2, num3):
    return maximum(maximum(num1, num2),num3) 


def maximum_input():
    num1= float(input("num1"))
    num2= float(input("num2"))
    num3= float(input("num3"))
    
    return maximum3(num1, num2, num3)