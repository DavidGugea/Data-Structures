class CircularBuffer(object):
    def __init__(self, capacity, resetBuffer_AfterFullDeletion = True):
        self.capacity = capacity

        # Set the head & the tail at the beginning to None
        self.head = -1 
        self.tail = -1

        # Create a list that will represent all the items that will be enqueued & dequeued from the buffer. By default all it's items are None. In time, when we will deque or enqueue something using the circular buffer, the self.counter property will change 
        self.items = [None] * self.capacity
        self.counter = 0

        # "resetBuffer_AfterFullDeletion" indicates if we have to reset the head & tail both being to -1, so the default buffer after every item has been deleted, or if we should keep the indexes
        self.resetBuffer_AfterFullDeletion = resetBuffer_AfterFullDeletion

        # Indicates if the buffer is empty or not by keeping track of the counter of the items
        self.IS_EMPTY_FLAG = False

    def is_empty(self):
        # Return is_empty if the head & tail are both -1 ( this is how the buffer indexes start ) or if the is_empty_flag True is or not 
        return ( self.head == -1 and self.tail == -1 ) or self.IS_EMPTY_FLAG

    def is_full(self):
        '''
        The buffer is full when :
            - > the tail is right behind the head, we can't enqueue any other items, we can't overwrite them. / The counter reached the capacity
            - > The tail reached the end and the head is still at the start
        '''
        return ( self.tail == self.head - 1 ) or ( self.tail == self.capacity - 1 and self.head == 0 ) or ( self.counter == self.capacity ) 
    
    def getBufferItems(self):
        ''' Returns the list with all the items ( including the 'None') '''
        return self.items

    def getBufferIntervalItems(self):
        ''' Returns the items that are in the circular buffer and that are not None, the complete circle '''
        if self.head <= self.tail:
            return self.items[self.head:self.tail + 1]
        else:
            return self.items[self.head:] + self.items[:self.tail + 1]

    def getHead(self):
        ''' Return a dict. with the index as key & the item in the buffer as value '''
        return { self.head : self.items[self.head] }

    def getTail(self):
        ''' Return a dict. with the index as key & the item in the buffer as value '''
        return { self.tail : self.items[self.tail] }  


    def resetBuffer(self):
        ''' Resets the buffer to it's default indexes '''
        self.head = -1
        self.tail = -1

    def enqueue(self, item):
        # Raise an error if the buffer is full and we try to add something to it
        if self.is_full():
            raise OverflowError("The buffer is full.You can't add any new items to it.")

        # At the beginning, the head will pe set on -1, set it to 0 now
        if self.head == -1:
            self.head = 0

        # Increase the index of the tail before we change the item at the tail index 
        self.tail += 1

        # In case that the self.tail reached the capacity, change the tail to the beginning of the buffer
        if self.tail == self.capacity:
            self.tail = 0 
    
        # Change the "None" value at the self.tail index to the item
        self.items[self.tail] = item

        # Increase the counter of the items, because we replaced a "None" value with a new item and reset the "IS_EMPTY_FLAG" because we have a new item to the buffer 
        self.counter += 1
        self.IS_EMPTY_FLAG = False

    def dequeue(self):
        # Raise an exception in case that the buffer is empty and we try to dequeue items from the buffer 
        if self.is_empty():
            raise Exception("The buffer is empty. You can't dequeue any items from it.") 

        # Set the current head value to none
        self.items[self.head] = None

        # Increase the head index. In case that the head reached the capacity, we will reset the head to be 0
        self.head += 1
        if self.head == self.capacity:
            self.head = 0
    
        # Decrement the counter because we dequeued an item so we have instead of the item the value "None", so one less item, so decrement the counter value
        self.counter -= 1

        # We decrement the counter value, so, in case that it's 0, the buffer will be empty
        if self.counter <= 0:
            # The buffer is empty so set the IS_EMPTY_FLAG to be True
            self.IS_EMPTY_FLAG = True
            # In case that the user chose to reset the buffer after a full deletion, call the self.resetBuffer() method.
            if self.resetBuffer_AfterFullDeletion:
                self.resetBuffer()
