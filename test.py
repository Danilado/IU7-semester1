arr = [(1, 1)] + [None]*9

print(arr)

for i in range(1, 10):
    arr[i] = (arr[i-1][1]*2 + arr[i-1][0],
              arr[i-1][0]**2*2 + arr[i-1][1])

print(*arr, sep='\n')
