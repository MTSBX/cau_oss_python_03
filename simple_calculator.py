
def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def plus(number_a,number_b):
    plus_sum=int(number_a)+int(number_b)
    return plus_sum

def subtract(number_c,number_d):
    subtract_sum=int(number_c)-int(number_d)
    return subtract_sum

 #mul = lambda x,y:x*y
 #div = lambda x,y:x/y
 #mod = lambda x,y:x%y

while True:
    op = input("input operation:")
    if op == "end":
        break
    elif op == "+":
        num1,num2,ret = arithmetic_ops(plus) 
    elif op == "*":
        #num1,num2,ret= arithmetic_ops(mul) 
        num1,num2,ret= arithmetic_ops(lambda x,y:x*y) 
    elif op == "-":
        num1,num2,ret = arithmetic_ops(subtract)
    elif op == "/":
        #num1,num2,ret= arithmetic_ops(div)
        num1,num2,ret= arithmetic_ops(lambda x,y:x/y) 
    elif op == "%":
        #num1,num2,ret= arithmetic_ops(mod)
        num1,num2,ret= arithmetic_ops(lambda x,y:x%y) 
    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}") 

print("Exit program")
