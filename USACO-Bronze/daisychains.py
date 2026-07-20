N = int(input())
flowers = list(map(int, input().split()))

AverageFlowers = 0
for i in range(N):
    for j in range(i, N):
        average_petals = sum(flowers[i : j + 1]) / (j - i + 1)

        for place in range (i, j + 1):
            if flowers[place] == average_petals:
                AverageFlowers += 1
                break

print(AverageFlowers)