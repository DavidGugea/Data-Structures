import collections

def space():
    for i in range(3):
        print()

de = collections.deque(list(range(1, 5)))
print("START -- > {0}".format(de))

space()

print("appendLeft('A') < - > append('B')")
de.appendleft("A")
de.append("B")
print(de)

space()

print("pop() < - > popleft()")
de.popleft()
de.pop()
print(de)

space()

print("extendleft(['A']) < - > extend(['B'])")
de.extendleft(["A"])
de.extend(["B"])
print(de)

space()

print("remove('A') < - > remove('B')")
de.remove("A")
de.remove("B")
print(de)

space()

print("insert(3, 'A')")
de.insert(3, "A")
print(de)

space()

print("de.count('A') -- > {0}".format(de.count("A")))

space()

print("de.index('A') -- > {0}".format(de.index("A")))

space()

print("de.rotate(2)")
de.rotate(2)
print(de)

space()

print("reverse()")
de.reverse()
print(de)


space()