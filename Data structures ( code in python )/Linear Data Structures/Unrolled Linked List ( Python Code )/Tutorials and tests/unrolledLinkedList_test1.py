import random

class QuickSort(object):
    def medianOfThree(self, arr, low, high):
        if len(arr[low:high]) >= 3:
            start_middle_high = [ arr[low], arr[ ( low + high ) // 2 ], arr[high] ]
            start_middle_high.sort()

            return arr.index(start_middle_high[1])
        else:
            return random.randint(low, high)
    def partition(self, arr, low, high):
        # Get the pivot index 
        pivotIndex = self.medianOfThree(arr, low, high)

        # Get the pivot value from the array using the pivot index
        pivot = arr[pivotIndex]

        # Swap the pivot with the last element from the array
        arr[high], arr[pivotIndex] = arr[pivotIndex], arr[high]

        # Update the pivot index
        pivotIndex = high

        # Create two pointers that will scan the array #########
        LP = low        # Left pointer  ( swaps var > pivot ) ##
        RP = high - 1   # Right pointer ( swaps var < pivot ) ##
        ########################################################

        # Scan the array using the pointers & swap the necessary values that must be swaped. At the end you will arrive with the index for the pivot
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap the values at the 2 pointers
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment the left pointer
                LP += 1

                # Decrement the right pointer
                RP -= 1
            else:
                if arr[LP] < pivot:
                    # Increment the left pointer 
                    LP += 1


                if arr[RP] > pivot:
                    # Decrement the right pointer
                    RP -= 1

        # Swap the left pointer value with the pivot 
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Update the pivot index
        pivotIndex = LP

        # Return the pivot index ( border index ) 
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low <= high:
            # Get the partition index
            partitionIndex = self.partition(arr, low, high)

            # Quick sort both halves of the list
            self.quickSort(arr, low, partitionIndex - 1)
            self.quickSort(arr, partitionIndex + 1, high)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class nodeBucket(object):
    def __init__(self, title, capacity = None):
        self.bucketItems = list()
        self.capacity = capacity
        self.title = title

        self.next = None # represents a pointer to the next bucket 

    def getSize(self):
        return len(self.bucketItems)

    def __len__(self):
        return len(self.bucketItems)

    def appendToBucket(self, item): 
        if self.capacity is None:
            self.bucketItems.append(item)
        else:
            if len(self) >= capacity:
                raise OverflowError("The bucket is full, you can't add anything to it.") 

            self.bucketItems.append(item) 

    def extendBucketWithList(self, extend_list):
        if self.capacity is not None and len(self) + len(extend_list) > self.capacity:
            raise Exception("The extend list is too big for the node bucket.")
        else:
            self.bucketItems.extend(extend_list)
    
    def getItems(self):
        return self.bucketItems

class UnrolledLinkedList(object):
    def __init__(self, individualBucketCapacity = None):
        self.individualBucketCapacity = individualBucketCapacity
        self.numberOfNodeBuckets = 0

        self.headBucket = None
    def appendBucket(self, title):
        if self.numberOfNodeBuckets == 0:
            self.headBucket = nodeBucket(title, self.individualBucketCapacity)
        else:
            indexTrack = 0
            current = self.headBucket
            while indexTrack < self.numberOfNodeBuckets - 1:
                indexTrack += 1
                current = current.next

            print(current)
    

        self.numberOfNodeBuckets += 1
    def getBucketsData(self):
        if self.numberOfNodeBuckets == 0:
            return list()

        bucketsData = list()

        indexTrack = 0
        current = self.headBucket

        while indexTrack < self.numberOfNodeBuckets:
            bucketsData.append(current.getItems())

            indexTrack += 1
            current = current.next

        return bucketsData

ULL = UnrolledLinkedList()
print("START ULL -- > {0}".format(ULL.getBucketsData()))

for i in range(3):
    print()

print(ULL.headBucket)
print(bool(ULL.headBucket))

ULL.appendBucket("HEAD-BUCKET")

print(ULL.headBucket)
print(bool(ULL.headBucket))

for i in range(3):
    print()

print("END ULL -- > {0}".format(ULL.getBucketsData()))

