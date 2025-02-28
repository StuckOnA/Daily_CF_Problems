from math import gcd

n, k = map(int, input().split())
a, b = map(int, input().split())

v = n * k

mi, ma = n * k, 0

for i in range(n):
  x = i * k + a - b
  res = v // gcd(v, x)
  if res < mi: mi = res
  if res > ma: ma = res
  x = i * k + a + b
  res = v // gcd(v, x)
  if res < mi: mi = res
  if res > ma: ma = res

print(mi, ma)
