N = int(input())

if N == 0:
    print('E')
elif 1 <= N <= 35:
    print('D')
elif 35 <= N <= 60:
    print('C')
elif 61 <= N <= 85:
    print('B')
else:
    print('A')
