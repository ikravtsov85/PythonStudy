A = int(input())
B = int(input())
C = int(input())

costR = A * C * 100
costK = B * C
cost = costR + costK
print(cost // 100, cost % 100)
