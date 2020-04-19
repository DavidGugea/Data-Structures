def arrayAdvance_myCode(array):
    '''
    You are given an array of non-negative integers. For example:
        [3, 3, 1, 0, 2, 0, 1]
        
    Each number represents the maximum you can advance in the array.
    
    Question:
    Is it possible to advance from the start of the array to the last element ?
    
    https://www.youtube.com/watch?v=r7EzxgrYfNg&list=PL5tcWHG-UPH1YSW2RraQg2L2p5hQTIpNL
    '''

    currentIndex = 0
    
    # Create a dict that will keep track of the current values
    usedValues = dict()
    
    while currentIndex < len(array):
        var = array[currentIndex]
        varIndex = None
        
        if var not in usedValues.keys():
            # Var is not in the list, so therefore we can get the current index of it
            varIndex = array.index(var)
            
            # Insert varIndex in the dict
            usedValues[var] = varIndex
        else:
            # Get the var index from the last var index in the usedValues dict
            varIndex = array.index(var, usedValues[var] + 1)
            
            # Update last var index
            usedValues[var] = varIndex 
            
        # Create the border from the current index & var that we are at now
        border = varIndex + var + 1
        
        # If the border indicates that it reached the end, return True 
        if border >= len(array):
            return True
        
        # Get all the possible values that we can make from a certain point
        stepVars = array[varIndex + 1 : border]
        
        # If there are only 0's in the possible movement list, return False because we can't reach the end of the list
        if stepVars.count(0) == len(stepVars):
            return False
        
        # Get to the biggest element from all the possible steps that we can have
        # Exampel : [2, 4, 1, 1, 0, 2, 3], we begin at '2', the first element, so we can choose between 4 & 1 ( we can make 1 or 2 max. steps), so we will go to 4 because that is the biggest element in the steps that we can choose ( steps : [4, 1] )
        # After that, get the index of the max element that we chose and move the currentIndex to the index that we found for the biggest possible step element
        maxVar = max(stepVars)
        maxVarIndex = None
        
        if maxVar not in usedValues.keys():
            maxVarIndex = array.index(maxVar)
        else:
            maxVarIndex = array.index(maxVar, usedValues[maxVar] + 1)
        
        currentIndex = maxVarIndex

def arrayAdvance_tutorial(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1

    return furthest_reached >= last_idx
