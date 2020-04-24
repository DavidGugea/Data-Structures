import collections

def spaceUp():
    for i in range(3):
        print()

'''
The collections.deque() represents the deque data-structure. It has all the methods that a normal list has, but it also has :
        - popleft
        - appendleft
        - extendleft
        - rotate
'''

dq = collections.deque(list(range(1, 4)))

print("START -- > ")
print("DEQUE -- > {0}".format(dq))

spaceUp()

# We will jump straight to the new methods ( popleft, appendleft, extendleft & rotate )

# ~ popleft ~ #
print("print(dq.popleft())")
print("POPPED ITEM -- > {0}".format(dq.popleft()))
print("DEQUE -- > {0}".format(dq))

spaceUp()

# ~ appendleft ~ #
print("dq.appendleft(\"A\")")
dq.appendleft("A")
print("DEQUE -- > {0}".format(dq))

spaceUp()

# ~ extendleft ~ #
print("dq.extendleft(list(range(7, 11)))")
dq.extendleft(list(range(7, 11)))
print("DEQUE -- > {0}".format(dq))

spaceUp()

# ~ rotate ~ #
print("dq.rotate(5)")
dq.rotate(5)
print("DEQUE -- > {0}".format(dq))

spaceUp()
