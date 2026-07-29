"""Harn 10"""
n = int(input())
n1 = round(n // 10) * 10
numin = []

for n1 in range(n1,-10,-10):
    numin.append(n1)
print(*numin)
