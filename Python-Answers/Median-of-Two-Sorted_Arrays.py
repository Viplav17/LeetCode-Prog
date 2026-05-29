num1 = [1, 3]
num2 = [2]

num3 = num1 + num2
num3.sort()

if len(num3) % 2 == 0:
    median = num3[len(num3) // 2 - 1] + num3[len(num3) // 2] / 2
else:
    median = num3[len(num3) // 2]

print(median)