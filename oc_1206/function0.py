# definition 더하기(숫자1,숫자2):
#     결과 =숫자1+숫자2
#     return 결과
# 결과1 = 더하기(2,3)
# 결과2 = 더하기(1,4)
def add(a,b):
    return a+b
result1 = add(2,3)
result2 = add(1,4)
print(result1)
print(result2)

# 재료가 있는 함수
def sayHello():
    return"helloooow"
result3 = sayHello()
print(result3)

# 재료가 없는 함수
def printHello():
    print("hello")
printHello()