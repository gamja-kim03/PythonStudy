print('결과 : ')
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))

count = num1
s = 0

while count <= num2:
    s = s + count
    count = count + 1
print('누적합 : ', s)
