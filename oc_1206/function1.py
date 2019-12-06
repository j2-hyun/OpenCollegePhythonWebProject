# 이 함수는 두개의 숫자 재료를 건네받아 곱한 값과 나눈 값을 고객에게 리턴해준다
def multiplyAndDivide(a,b):
    multiplyResult=a*b
    divideResult=a/b
    return multiplyResult,divideResult

result = multiplyAndDivide(12,6)

# 여러개의 값을 리턴하는 함수는 튜플형태로 그 결과를 리턴한다
print(type(result))
print(result[0])
print(result[1])

# 이름을 지정해서 순서상관없이 넣을수 있음
result2 = multiplyAndDivide(b=3,a=12)
print(result2[0])
print(result2[1])