N = int(input())
daysSec = 86400
hours = N % daysSec // 3600
minutes = (N % daysSec - hours * 3600) // 60
seconds = (N % daysSec - hours * 3600 - minutes * 60)
print(hours, ':', sep='', end='')
print(minutes // 10, minutes % 10, ':', sep='', end='')
print(seconds // 10, seconds % 10, sep='')
