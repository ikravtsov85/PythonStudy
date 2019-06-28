H = int(input())
A = int(input())
B = int(input())
step = A - B
#print(6 % 7)
print(H - (H - A) // (A - B) + 1)
