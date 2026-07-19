def censor(S, T):
    t = len(T)
    output = ''

    for char in S:
        output += char
        if output.endswith(T):
            output = output[:-t]
    return output

import sys
sys.stdin = open('censor.in', 'r')
sys.stdout = open('censor.out', 'w')

S = input()
T = input()

print(censor(S, T))