class nodeBucket(object):
    def __init__(self, title, capacity = None):
        self.bucketItems = list()
        self.capacity = capacity
        self.title = title

        self.next = None

    def getSize(self):
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



x = nodeBucket("HEAD-BUCKET")
print(x)
print(bool(x))
