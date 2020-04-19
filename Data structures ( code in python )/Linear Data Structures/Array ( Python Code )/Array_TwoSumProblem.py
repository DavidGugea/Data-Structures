import itertools

# Given a sorted array of integers, return the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice

# Time complexity  : O(n)
# Space complexity : O(1)
def twoSumProblem_myCode(array, target):
    for permutation in list(itertools.permutations(array, 2)):
        if sum(permutation) == target:
            return tuple(permutation)
<<<<<<< HEAD
    return None
=======
    return None 
>>>>>>> Array_PythonCode

def twoSumProblem_noItertools_myCode(array, target):
    # Get the difference of numbers using a hashtable
    ht = dict()
    
    for var in array:
        if var in ht.keys():
            print(ht.get(var), var)
            return True
        else:
            ht.setdefault(target - var, var)

# Time complexity  : O(n^2)
# Space complexity : O(1)
def twoSumProblem_bruteForce_tutorial(array, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
            
    return False
            
# Time complexity  : O(n)
# Space complexity : O(n)
def twoSumProblem_hash_table_tutorial(array, target):
    ht = dict()
    
    for i in range(len(A)):
        if A[i] in ht.keys():
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
        
    return False
    
def two_sum_tutorial(array, target):
    # Works only for sorted lists
    i = 0
    j = len(array) - 1
    
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            # Increment left pointer
            i += 1
        elif A[i] + A[j] > target:
            # Decrement right pointer
            j -= 1
            
    return False
            
            

A = [-2, 1, 2, 4, 7, 11]
target = 10

print(two_sum_tutorial(A, target))