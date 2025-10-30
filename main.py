def calculator(n1,n2,op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return 'Error'

def calculator_pr(n):
    return n

print(calculator_pr(calculator(1,2,'+')))
print(calculator_pr(calculator(2,1,'-')))
print(calculator_pr(calculator(2,1,'*')))
print(calculator_pr(calculator(4,2,'/')))
print(calculator_pr(calculator(4,2,'////')))