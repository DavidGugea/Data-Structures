class NodeBucket(object):
    def __init__(self):
        self.bucketItems = list()
        self.next = None

    def get_items(self):
        return self.bucketItems

class UnrolledLinkedList(object):
    def __init__(self):
        self.headBucket = None
        self.counter = 0

    def appendBucket(self):
        if not self.headBucket:
            self.headBucket = NodeBucket()
        else:
            current = self.headBucket

            while current.next:
                current = current.next
            
            current.next = NodeBucket()

        self.counter += 1

    def appendItemAtBucket(self, bucketIndex, item):
        if not 0 <= bucketIndex < self.counter:
            raise IndexError("The index is either too big for the unrolled linked list or too small ( < 0 )")
        else:
            indexTrack = 0
            current = self.headBucket

            while indexTrack < bucketIndex:
                current = current.next
                indexTrack += 1
            
            current.bucketItems.append(item)

    def deleteAtIndex(self, index):
        if not 0 <= index < self.counter:
            raise IndexError("The index is either too big for the unrolled linked list or too small ( < 0 )")
        elif index == 0:
            temp = self.headBucket
            self.headBucket = temp.next
        
            temp = None
        else:
            current = self.headBucket
            prev = None
            indexTrack = 0
    
            while indexTrack < index:
                prev = current
                current = current.next

                indexTrack += 1

            prev.next = current.next
            current = None

        self.counter -= 1

    def get_ULL_items(self):
        items_list = list()
        current = self.headBucket

        while current:
            items_list.append(current.get_items())

            current = current.next

        return items_list
