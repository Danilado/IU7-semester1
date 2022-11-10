"""
вставить в упорядоченный по 
возрастанию массив A число R
расширенный массив напечатать
"""

from turtle import pos


a = [i for i in range(100) if i != 42]
r = 42

n = len(a)

pos = len(a)//2

while not (a[pos] < r < a[pos+1]):
    print(pos)
    if r > a[pos]:
        pos *= 1.5
        pos = int(pos)
    elif r < a[pos]:
        pos //= 1.5

a.insert(pos, r)

print(a)
