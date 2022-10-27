# n студентов
# t[i] = время обслуживания i-го студента
# Даны t[i] in R
# требуется получить c[i]
# время пребывания студента в очереди

n = 100
t = [i % 20 for i in range(100)]
c = []
mintime = t[0]
mintime_n = 0

cur_time = 0

for i in range(n):
    c.append(cur_time)
    cur_time += t[i]
    if t[i] < mintime:
        mintime = t[i]
        mintime_n = i

print(*c)
print(mintime_n)
