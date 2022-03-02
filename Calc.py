import math

num1 = int(input('What is your first number?'))
num2 = int(input('What is your second number?'))
prob = input('What math problem do you want to do?: +, -, *, or / ')

if prob == '+':
    print('The answer is',num1+num2)
elif prob == '-':
    print('The answer is',num1-num2)
elif prob == '*':
    print('The answer is',num1*num2)
elif prob == "/":
    print('The answer is',num1/num2)
elif prob =='/':
        try:
            print('The awnswer is = ',num1/num2)
        except Exception as prob:
            print('0 cannot be entered as denominator, enter something else and try again.')
