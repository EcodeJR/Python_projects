print("Calculator")

value_one = int(input("Enter a value:\n"))
actioncal = input("ADD(+),SUB(-),DIV(/).MULT(*):\n")
value_two = int(input("Enter your second value:\n"))
add = value_one + value_two
sub = value_one - value_two
div = value_one / value_two
mult = value_one * value_two

if actioncal == "+":
    print(add)
    
if actioncal == "-":
    print(sub)
    
if actioncal == "/":
    print(div)
    
if actioncal == "*":
    print(mult)
