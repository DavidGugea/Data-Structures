class NodeBucket(object):
    def __init__(self, capacity = None):
        # Define the capacity, by default it is None ( that means that bucket doesn't have any capacity. You can store as many items as you wish ). If it's not none that it has a limit
        self.capacity = capacity

        # Create the node bucket items list
        self._bucketItems = list()

        # Create the pointer for the next bucket
        self.next = None

    def getSize(self):
        return len(self._bucketItems)

    def getItems(self):
        return self._bucketItems

    def appendItemToBucket(self, item):
        if self.capacity is None:
            # Just append the item to the bucket items, we don't care about the number of items present in the bucket
            self._bucketItems.append(item)
        else:
            # Check if the bucket reached it's capacity. If that is the case, raise an OverflowError
            if len(self._bucketItems) >= self.capacity:
                raise OverflowError("The bucket has reached it's capacity of {0} items".format(self.capacity))
            
            # Append the item to the bucket items in case that the programm didn't stop at the OverflowError
            self._bucketItems.append(item)

    def extendItemWithList(self, item_list):
        if type(item_list) != list:
            raise ValueError("The given item_list argument used to extend the item list for the bucket must be a list ( have a list type )")

        if self.capacity is None:
            # Just extend the list because there is no capacity, hence there is nothing to check
            self._bucketItems.extend(item_list)
        else:
            # Check if the length of the node bucket summed with the lenght of the item_list reached is more or equal than the capacity.. If that is the case, raise an OverflowError
            if len(self._bucketItems) + len(item_list) > self.capacity:
                raise OverflowError("The given item_list that must be extended with the list of the unrolled linked list is too big.")
            
            # If the programm didn't stop because of the overflow error, extend the bucket items list with the item_list
            self._bucketItems.extend(item_list)

    def insertItemAtIndex(self, index, item):
        # Check the index
        if not 0 <= index < len(self._bucketItems):
            raise IndexError("The given index is either too big for the unrolled linked list or too small ( < 0 )")

        # Check if the ULL has reached it's maximum capacity
        if len(self._bucketItems) == self.capacity:
            raise OverflowError("The bucket items reached the maximum capacity of {0} items".format(self.capacity))

        self._bucketItems.insert(index, item)

class UnrolledLinkedList(object):
    def __init__(self, defaultCapacity = None, ULL_CAPACITY = None):
        # Define the default capacity | The default capacity is the capacity that each individual box will have when you will use ULL.appendBucket() without an argument
        self.defaultCapacity = defaultCapacity

        # Define the ULL_CAPACITY | The ULL_CAPACITY means the number of buckets that are allowed to be in the ULL
        self.ULL_CAPACITY = ULL_CAPACITY
        
        # Increment self.bucketCounter when adding a new bucket to the ULL | Decrement self.bucketCounter when deleting a bucket from the ULL
        self.bucketCounter = 0

        # Create the headBucket | By default is None
        self.headBucket = None

    def appendBucket(self, individualBucketCapacity = None):
        # Check the ULL_CAPACITY
        if self.ULL_CAPACITY:
            if self.bucketCounter >= self.ULL_CAPACITY:
                raise OverflowError("The unrolled linked list reached its capacity of {0} buckets".format(self.bucketCounter))

        newBucket = None
        # Check if the arg "individualBucketCapacity" is None, if it is None, use the 'self.defaultCapacity' that is used for each bucket that doesn't have an individual capacity. If the arg "individualBucketCapacity" is not None, set it to the newBucket
       
        if individualBucketCapacity:
            newBucket = NodeBucket(individualBucketCapacity)
        else:
            newBucket = NodeBucket(self.defaultCapacity)

        # Check if there is a head bucket, if there is not create one, otherwise iterate over the ULL and append it
        if not self.headBucket:
            self.headBucket = newBucket
        else:
            # Iterate over the unrolled linked list to get to the last list ( start with the headBucket and iterate to the last item using .next )
            current = self.headBucket

            while current.next:
                current = current.next

            # Set the next element of the last bucket to the newBucket that we created above
            current.next = newBucket

        # Increase the bucket counter 
        self.bucketCounter += 1 

    def appendItemAtBucket(self, bucketIndex, item):
        # Check the bucket index
        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big or too small ( < 0 )")

        # Iterate over the ULL to find the bucket at the index
        current = self.headBucket
        indexTrack = 0

        while indexTrack < bucketIndex:
            current = current.next
            indexTrack += 1

        # Append the item
        current.appendItemToBucket(item)

    def deleteBucketAtIndex(self, bucketIndex):
        # Check the bucket index
        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The given bucket index is either too big for the ULL or too small ( < 0 )")

        # Check if the bucket index is the head bucket ( 0 ), if that is the case then change the head bucket, otherwise iterate over the entire ULL till you get to the given index and then change the properties of prev & current bucket nodes
        if bucketIndex == 0:
            temp = self.headBucket
            self.headBucket = temp.next
            temp = None
        else:
            prev = None
            current = self.headBucket
            indexTrack = 0
            
            while indexTrack < bucketIndex:
                prev = current
                current = current.next

                indexTrack += 1

            prev.next = current.next
            current = None

        # Decrement the bucket counter
        self.bucketCounter -= 1

    def getBucketItemsList(self):
        bucketItems = list()
        
        # Start with the head bucket and iterate to the end while adding the items for each bucket
        current = self.headBucket

        while current:
            bucketItems.append(current.getItems())
            current = current.next

        return bucketItems
