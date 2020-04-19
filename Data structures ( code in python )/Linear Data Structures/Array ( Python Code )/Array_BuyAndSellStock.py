import itertools
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Space complexity : O(n^3)
# Time complexity  : O(n^3)
def BuyAndSell_Stock_MyCode_bruteForce_1(array):
    ht = dict()
    usedValues = dict()
    
    for price in A:
        varIndex = None
        
        if price in usedValues.keys():
            varIndex = array.index(price, usedValues[price] + 1)
        else:
            varIndex = array.index(price)
        usedValues[price] = varIndex
        
        for comparePrice in A[varIndex + 1:]:
            ht[comparePrice - price] = (price, comparePrice)
            
    
    return (max(ht.keys()), ht[max(ht.keys())])

# Time complexity  : O(n^2)
# Space complexity : O(1)
def BuyAndSell_Stock_MyCode_bruteForce_2(array):
    max_ = 0
    
    for i in list(range(0, len(array) - 1)):
        for j in array[i+1:]:
            if j - array[i] > max_:
                max_ = j - array[i]
            
    return max_

# Time & space complexity considering itertools.permutations O(1)
# Space complexity : O(n) 
# Time complexity  : O(n)
def BuyAndSell_Stock_MyCode_itertools(array):
    ht = dict()
    
    for permutation in list(itertools.permutations(array, 2)):
        if array.index(permutation[0]) < array.index(permutation[1]):
            ht[permutation[1] - permutation[0]] = permutation
            
    return (max(ht.keys()), ht[max(ht.keys())])


def BuyAndSellStock_myCode(array):
    smallestStock = array[0]
    biggest_StockDiff = 0
    
    for stock in array:
        if stock < smallestStock:
            smallestStock = stock
            continue
        
        if stock - smallestStock > biggest_StockDiff:
            biggest_StockDiff = stock - smallestStock
            
    return biggest_StockDiff
    
''''''''''' tutorial '''''''''''

# Time complexity  : O(n^2)
# Space complexity : O(1)
def buy_and_sell_once_BruteForce_tutorial(A):
    max_profit = 0
    
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    
    return max_profit

# Time complexity  : O(n)
# Space complexity : O(1)
def buy_and_sell_once_Alg_tutorial(A):
    max_profit = 0.0
    min_price = A[0]
    
    for price in A:
        min_price = min([min_price, price])
        max_profit = max([max_profit, price - min_price])
        
        continue 
    
    return max_profit

print(buy_and_sell_once_Alg_tutorial(A))