

N = int(input())
total_lost = 0

for _ in range(N):
    inputs = input().split()
    A = int(inputs[0])
    B = int(inputs[1])
    S = inputs[2]

    if S == "keep":
        total_lost += (B - A)
print(total_lost)