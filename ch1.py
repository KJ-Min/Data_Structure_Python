def med3(a, b, c):
    if (b >= a and a >= c) or (c >= a and a >= b):
        return a
    elif (a >= b and b >= c) or (c > b and b >= a):
        return b
    else:
        return c


print("세 정수를 입력하세요.")
a = int(input("정수 a를 입력하세요 :"))
b = int(input("정수 b를 입력하세요 :"))
c = int(input("정수 c를 입력하세요 :"))
print(f"중앙값은 {med3(a,b,c)}입니다.")
