import math

def sockMerchant(ar, n): 
    
    new_list = []
    paired_list = []
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i + 1, n, 1):
            if ar[i] == ar[j]:
                visited[j] = True
                count += 1        
        new_list.append(count)
        pair = 0
        for m in new_list:
            pairs = m/2
            pair = math.trunc(pairs)
        paired_list.append(pair)
    print(sum(paired_list))



if __name__ == '__main__': 
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20] 
    n = len(ar) 
    sockMerchant(ar, n) 
      