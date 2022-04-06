while 0 < 1:
   print('Please enter first number')
   try:
       a = float(input())
       break
   except:
        print('Your number is worng')
    
while 0 < 1:
    print('Please enter operator')
    try:
       c = str(input())
    except:
        print('Your operator is worng')

    if c == '+' or c == '-' or c =='*' or c == '**' or c == '/' or c == '//' or c == '%':
        break
    else:
        print('Your operator is worng')


while 0 < 1:
   print('Please enter second number')
   try:
       b = float(input())
       break
   except:
        print('Your number is worng')


if c == '+':
    print('result: ', a + b)
elif c == '-':
    print('result: ',a - b)
elif c == '*':
    print('result: ',a * b)
elif c == '/':
    print('result: ',a / b)
elif c == '%':
    print('result: ',a % b)
elif c == '**':
    print('result: ',a ** b)
elif c == '//':
    print('result: ',a // b)
else:
    print('error(idk)')