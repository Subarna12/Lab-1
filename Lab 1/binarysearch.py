# Best Case: O(1)
# Worst Case: O(log(N))
# Average Case: O(log(N))
def iterative_binary_search(A, l, h, target):

    while l <= h:
        mid = (l + h) // 2

        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
            
    return -1
    

def recursive_binary_search(A, l, h, target):
    

    if l <= h:
        mid = (l + h) // 2

        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return recursive_binary_search(A, l, mid - 1, target)
        return recursive_binary_search(A, mid + 1, h, target)
    
    return -1 
