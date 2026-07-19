import sys

num_of_balls, num_of_colours = map(int, sys.stdin.readline().strip().split())

max_sizes = {}

for _ in range(num_of_balls):
    colour, size = map(int, sys.stdin.readline().strip().split())

    if size > max_sizes.get(colour, -1):
        max_sizes[colour] = size
Final = [max_sizes.get(x, -1) for x in range(1, num_of_colours + 1)]
print(*Final)