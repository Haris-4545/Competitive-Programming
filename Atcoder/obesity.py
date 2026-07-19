Height_cm, Weight = map(int, input().split())

if 10000 * Weight >= 25 * (Height_cm ** 2):
  print("Yes")
else:
  print("No")