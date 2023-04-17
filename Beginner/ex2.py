fNumber = float(input("Please type first number "))
sNumber = float(input("Please type second number" ))
operator = input("Please choose operator (+,-,*,/)" )

if operator == "+":
    result = fNumber + sNumber
    print(result)

elif operator == "-":
    result = fNumber - sNumber
    print(result)

elif operator == "*":
    result = fNumber * sNumber
    print(result)

elif operator == "/":
    if sNumber == 0:
        print("Error: Division number cannot be ZERO")
    else:
        result = fNumber / sNumber
        print(result)

else :
    print("Error: Invalid operator")

