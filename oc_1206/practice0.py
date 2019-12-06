def calc(calcType, a, b):
    if calcType == "더하기":
        return a + b
    if calcType == "빼기":
        return a - b
    if calcType == "곱하기":
        return a * b
    if calcType == "나누기":
        return a / b

a = input("계산정보를 입력하세요: ")
받은것들 = a.split()
print(a)
calcType = 받은것들[0]
b= 받은것들[2]
a= 받은것들[1]
a=int(a)
print(a)
print(type(a))
b=int(b)
print(b)
print(type(b))
print(calcType)

result = calc(calcType, a, b)
result=str(result)
print (type(result))
print("계산결과 : " + result)