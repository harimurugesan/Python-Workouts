def binary_search(vector, el):
    low = 0
    high = len(vector)
    while low < high:
        mid = int((low+high)/2)
        
        if vector[mid]<el:
            low = mid + 1
        elif vector[mid]>el:
            high = mid
        else:
            return mid + 1
    
    assert low==high, "low != high"
    if low < len(vector):
    	return low + 1
    else: return -1
 
def main():
    T = int(raw_input())
    worths = (raw_input()).split(' ')
    worths[0] = int(worths[0])
    for i in range(T-1):
        worths[i+1] = worths[i] + int(worths[i+1])
        
    Q = int(raw_input())
 
    queries = []
    for _ in range(Q):
        queries.append(int(raw_input()))
 
    for q in queries:
        result = binary_search(worths, q)
        if result==T+1:
        	print -1
        else: print result
        	
    
if __name__=="__main__":
    main()