def arbitraryPrecisionIncrement_myCode(A):
    memoryValue = 0
    A = A[::-1]
    index = 0
    
    while index < len(A):
        
        if memoryValue == 0 and index > 0:
            break
        
        value = None
        if index == 0:
            value = A[index] + 1
        else:
            value = A[index] + memoryValue
            
        if value >= 10:
            memoryValue = int(str(value)[0])
            A[index] = int(str(value)[1])
        else:
            A[index] = value
            memoryValue = 0
                    
        index += 1

        if index == len(A) and memoryValue != 0:
            A.append(memoryValue)
            break
        
    A = A[::-1]
    
    return A

def arbitraryPrecisionIncrement_myCode_2(A):
    return list(map(int, list(str(eval(''.join(map(str, A))) + 1))))
    
def arbitraryPrecisionIncrement_tutorial(A):
    A[-1] += 1
     
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        
        A[i] = 0
        A[i - 1] += 1
        
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    
    return A
        
A = [1, 4, 9]
A = arbitraryPrecisionIncrement_myCode(A)
print(A)
