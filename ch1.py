def med3(a, b, c):
    if a > b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c

    elif a > c:
        return a

    elif b > c:
        return c

    else:
        return b


print("세 정수를 입력하세요.")
a = int(input("정수 a를 입력하세요 :"))
b = int(input("정수 b를 입력하세요 :"))
c = int(input("정수 c를 입력하세요 :"))
print(f"중앙값은 {med3(a,b,c)}입니다.")
