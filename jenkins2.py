import sys
def add_numbers(a, b):
    return a + b
def sub_number(a,b):
    return a-b 
def mul_numbers(a, b):
    return a*b
def div_number(a,b):
    return a/b    
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    result1 = add_numbers(num1, num2)
    
    print("=================================")
    print("Addition Result")
    print("=================================")
    
    print(f"addition : {result1}")
    

    result2 = sub_numbers(num1, num2)
    print("=================================")
    print("Subraction Result")
    print("=================================")
    
    print(f"subtraction : {result2}")

    result3 =mul_numbers(num1, num2)
    print("=================================")
    print("Multiplication Result")
    print("=================================")
    
    print(f"Multiplication : {result3}")

    result4 = div_numbers(num1, num2)
    print("=================================")
    print("Division Result")
    print("=================================")
    
    print(f"Division : {result4}")