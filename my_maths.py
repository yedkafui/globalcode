def calculate(operation,num1,num2):
    operation = str(input('Your operation(add,subract,divide,multiply): ')).upper()
    num1 = int(input("First number: "))
    num2 = int(input("second number: "))
    
    if operation == "ADD":
        answer = num1 + num2
        return answer
    elif operation == "SUBTRACT":
         answer = num1 - num2
         return answer
    elif operation == "MULTIPLY":
         answer = num1 * num2
         return answer
    elif operation == "DIVIDE":
         answer = num1 / num2
         return answer
    else:
        print("Can't perform operation!! Check operation")


answer = calculate('subtract',4,4)
print(f"{'Answer: '}{answer}")