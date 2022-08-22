import math
for i in range(int(input())):
    a = int(input())
    if a==1 or a==2:
        print(f"Case #{i+1}: {1}")
    else:
        print(f"Case #{i+1}: {math.ceil(a/5)}")
