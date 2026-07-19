import sys

input = sys.stdin.readline

X = int(input())
Y = int(input())
L = int(input())
R = int(input())
A = int(input())
B = int(input())

total_fee = 0
for hour in range(A, B):
    if L <= hour < R:
        total_fee += X
    else:
        total_fee += Y
print(total_fee)