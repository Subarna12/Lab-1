# Best Case: O(1)
# Worst Case: O(N)
# Average Case: O(N)

def linear_search(A, target):
  
    for i, elem in enumerate(A):
        if A[i] == target:
            return i

    return -1
    

