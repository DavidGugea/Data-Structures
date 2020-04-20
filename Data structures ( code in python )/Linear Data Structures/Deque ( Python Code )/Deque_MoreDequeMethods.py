# importing 'collections' for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurence of 4 
print("The number 4 first occurs at a position : ")
print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)

# printing modified deque
print("The deque after inserting 3 at 5th position is : ")
print(de)

# using count() to count the occurences of 3
print("The count of 3 in deque is : ")
print(de.count(3))

# using remove() to remove the first occurence of 3
de.remove(3)

# printing modifed deque
print("The deque after deleting first ocucrence of 3 is :")
print(de)

for i in range(5):
    print()

de = collections.deque([1, 2, 3])

# using extend() to add numbers to right end
# adds 4, 5, 6 to right end
de.extend([4, 5, 6])

# printing modifed deque
print("The deque after extending deque at end is : ")
print(de)

# using extendleft() to add numbers to left end
# adds 7, 8, 9 eto right end
de.extendleft([7, 8, 9])

# printing modifed deque
print("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print("The dque after totating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reverseing deque is : ")
print(de)