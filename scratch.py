import sys
num = int(input())

for i in range(num):
	a1, a2 = map(int, sys.stdin.readline().split())
	print(f"Case #{i+1}: {a1} + {a2} = " ,a1+a2)