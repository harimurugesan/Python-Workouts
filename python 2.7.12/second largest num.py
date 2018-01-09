n = int(raw_input())
arr = map(int, raw_input().split())
hi = max(arr)
hii = hi - 1
if hii in arr:
    print(hii)
else:
    while hii not in arr:
        hii -= 1
    print(hii)

    

    
