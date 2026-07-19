import sys

number_of_choices = int(sys.stdin.readline().strip())
choices = list(map(int, sys.stdin.readline().strip().split()))

if any(choice >=0 for choice in choices):
    print("No")
else:
    print("Yes")
