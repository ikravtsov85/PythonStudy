N = int(input())

days = N // 60 // 24
hours1 = N // 60 - days * 24
hours2 = N // 60
minutes = N - hours2 * 60
print(hours1, minutes)
