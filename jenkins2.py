import sys
def add_numbers(a, b):
    return a + b
def sub_numbers(a,b):
    return a-b
def mul_numbers(a,b):
    return a*b
def div_numbers(a,b):
    return a/b          
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = add_numbers(num1, num2)
    result1=sub_numbers(num1,num2)
    result2=mul_numbers(num1,num2)
    result3=div_numbers(num1,num2)
    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum          : {result}")
    print(f"sub        : {result1}")
    print(f"mul          : {result2}")
    print(f"div         : {result3}")