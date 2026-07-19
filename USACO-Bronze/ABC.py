nums = list(map(int, input().split()))

nums.sort()

#a is the least
a = nums[0]
#b is the second least
b = nums[1]
#c is the largest and is the last element minus a and b because A + B + C is the largest and then subtract A and B.
c = nums[-1] - a - b

print(a, b, c)