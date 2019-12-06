# for문을 이용하여 최댓값, 최솟값을 구하는 프로그램을 작성하시오.

# numbers 리스트
numbers = [1, 100, -1, 30, 5, 99, 45, 30, -2, -10]
max = numbers[0]
min = numbers[0]
# if numbers[1] > max:
#     max = numbers[1]
# else if numbers[2]>max

for number in numbers:
    if number > max:
        max = number

for number in numbers:
    if number < min:
        min=number

print("최대값은 "+ str(max))
print("최소값은 "+ str(min))