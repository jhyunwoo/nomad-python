def calculator():
    i=0
    while i==0:
        try:
            a = float(input("첫 숫자 입력 ㄱ"))
        except:
            print("잘못 입력함 다시해")
        else:
            break
    while i==0:
        b = input("연산기호 입력 ㄱㄱ")
        if b == "+" or "-" or "/" or "//" or "%" or "*" or "**":
            break            
        else:
            print("다시해 다시")
            
    while i==0:
        try:
            c = float(input("다음 숫자 입력 ㄱ"))
        except:
            print("잘못 입력함 다시해")
        else:
            break
    if b == "+":
        print(a+ c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print(a/c)
    elif b == "**":
        print(a**c)
    elif b == "//":
        print(a//c)
    elif b == "%":
        print(a%c)
        
calculator()
