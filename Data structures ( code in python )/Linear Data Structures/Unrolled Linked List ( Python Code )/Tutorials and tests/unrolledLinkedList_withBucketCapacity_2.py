class NodeBucket(object):
    def __init__(self, capacity = None):
        self.bucketItems = list()
        self.next = None
        
        self.capacity = capacity

    def getSize(self):
        return len(self.bucketItems) 

    def getItems(self):
        return self.bucketItems

    def appendBucketItem(self, item):
        if self.capacity is None:
            self.bucketItems.append(item)
        else:
            if len(self) >= self.capacity:
                raise OverflowError("The node bucket is full. You can't add any items to it. It has reached its capacity of {0}".format(self.capacity))

            self.bucketItems.append(item)

    def extendBucket_WithList(self, extend_list):
        if self.capacity is None:
            self.bucketItems.extend(item)
        else:
            if len(self) + len(extend_list) > self.capacity:
                raise OverflowError("The node bucket is full. You can't add any items to it. It has reached its capacity of {0}".format(self.capacity))

            self.bucketItems.extend(item)

    def insertItemAtIndex(self, item, index):
        if self.capacity is None:
            self.bucketItems.insert(index, item)
        else:
            if len(self) >= self.capacity:
                raise OverflowError("The node bucket is full. You can't add any items to it. It has reached its capacity of {0}".format(self.capacity))

class UnrolledLinkedList(object):
    def __init__(self, defaultCapacity = None, ULL_CAPACITY = None):
        # defaultCapacity represents the default capacity for each bucket added
        self.defaultCapacity = defaultCapacity

        # ULL_CAPACITY represents the maximum number of buckets that can be added in the ULL ( Unrolled Linked List )
        self.ULL_CAPACITY = ULL_CAPACITY
        self.bucketCounter = 0

        self.headBucket = None

    def appendBucket(self, individualBucketCapacity = None): 
        if self.ULL_CAPACITY != None:
            if self.bucketCounter >= self.ULL_CAPACITY:
                raise OverflowError("The number of buckets in the unrolled linked list has reached the maximum capacity of {0}".format(self.bucketCounter))
            
        appendBucketNode = None
        if individualBucketCapacity:
            appendBucketNode = NodeBucket(individualBucketCapacity)
        else:
            appendBucketNode = NodeBucket(self.defaultCapacity)

        if not self.headBucket:
            self.headBucket = appendBucketNode
        else:
            current = self.headBucket
            
            while current.next:
                current = current.next

            current.next = appendBucketNode
        
        self.bucketCounter += 1

    def appendItemAtBucket(self, bucketIndex, item):
        current = self.headBucket
        indexTrack = 0

        while indexTrack < bucketIndex:
            current = current.next
            indexTrack += 1

        current.appendBucketItem(item)

    def deleteBucket(self, bucketIndex):
        if bucketIndex == 0:
            temp = self.headBucket
            self.headBucket = temp.next
            temp = None
        else:
            current = self.headBucket
            prev = None

            indexTrack = 0

            while indexTrack < bucketIndex:
                prev = current
                current = current.next

                indexTrack += 1

            prev.next = current.next
            current = None

        self.bucketCounter -= 1

    def getBucketItems(self):
        bucketItems = list()

        current = self.headBucket
        
        while current:
            bucketItems.append(current.getItems())
            current = current.next

        return bucketItems

ULL = UnrolledLinkedList()

for i in range(5):
    ULL.appendBucket()

for i in range(5):
    ULL.appendItemAtBucket(i, chr(ord("A") + i))

print("START -- > ")
print(ULL.getBucketItems())
print("< -- START ")

for i in range(5):
    print()

ULL.deleteBucket(0)

for i in range(5):
    print()

print("END -- > ")
print(ULL.getBucketItems())
print("< -- END")
