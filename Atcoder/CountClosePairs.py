import sys

# USE 2 POINTERS, LEFT TO RIGHT IS LEAST TO GREATEST.
def CCC():
    N = int(sys.stdin.readline().strip())
    total_pairs = 0
    R = 1

    for i in range(1, N+1):
        if R < i:
            R = i
        while R + 1 <= N:
            print(f"? {i} {R + 1}", flush=True)
            response = sys.stdin.readline().strip()

            if response == "Yes":
                R += 1
            else:
                break
        total_pairs += (R - i)
    print(f"! {total_pairs}", flush=True)
if __name__ == "__main__":
    CCC()