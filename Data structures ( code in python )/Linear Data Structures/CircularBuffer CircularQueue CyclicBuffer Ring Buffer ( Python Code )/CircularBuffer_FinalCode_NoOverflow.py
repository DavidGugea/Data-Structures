class CircularBuffer(object):
    def __init__(self, capacity, resetAfter_FullDeletion = True):
        # Set the maximum capacity for the buffer 
        self.capacity = capacity

        # Create the head & tail pointers to indexes in the buffer. By default, both are 0 
        self.head = -1
        self.tail = -1

        # Create the items list. By default it will be full of 'None' * self.capacity. Each "None" represent an empty slot in the buffer
        self.items = [None] * self.capacity 

        # 'resetAFter_FullDeletion' represents if, after a full deletion ( so all slots in the buffer are empty and ready to be used ), if it is True, the self.head & self.tail will be both reseted to their default values of both being -1. Otherwise, self.head & self.tail will keep the same index values 
        self.resetAfter_FullDeletion = resetAfter_FullDeletion

        # The flag indicates if the buffer is empty or not. By default it is True because when we create the buffer it will be completly empty with all slots free and ready to use
        self.IS_EMPTY_FLAG = True

        # self.counter indicates how many used slots we have in the list. Each time we enqueue a new item, the counter will become bigger ( in case that we overwrite elements and the buffer is overflowed, the counter will stay at the maximum capacity -> min([self.capacity, self.counter + 1]) ). Each time we dequeue items from the buffer, the counter will decrement. In case that the counter will reach 0, we will know that the buffer is empty. 
        self.counter = 0

    def is_empty(self):
        ''' The buffer is empty if both, self.head & self.tail are -1 ( in the constructor both are set to -1 by default ) OR if the self.IS_EMPTY_FLAG is set on True '''
        return ( self.head == -1 and self.tail == -1 ) or self.IS_EMPTY_FLAG

    def getSize(self):
        ''' Return the self.counter property ''' 
        return self.counter

    def getBufferItems(self):
        ''' Return all the items from the buffer ( including the empty slots with 'None' values ) ''' 
        return self.items

    def getBufferIntervalItems(self):
        ''' Return the perfect interval where the buffer is not empty, all the slots from the buffer in perfect circular order '''
        if self.counter == self.capacity:
            return self.items
        elif self.head < self.tail:
            return self.items[self.head : self.tail + 1]
        elif self.tail < self.head:
            return self.items[self.head:] + self.items[:self.tail + 1]
    
    def resetBuffer(self):
        ''' Reset the buffer meaning that we reset both self.head & self.tail to -1 ( as by default in the constructor ) '''
        self.head = -1
        self.tail = -1

    def enqueue(self, item):
        # Increase the tail value and replace the empty ( 'None' value ) slot with the new item given in the *args. 
        self.tail += 1

        # In case that the tail reached it's maximum capacity, set it to 0, so that it will overwrite or fill ( in case of 'None' empty slot )the value
        if self.tail == self.capacity:
            self.tail = 0

        # At the beginning, both self.tail & self.head are set to 0. Make sure that the set will be set to 0 the first time we will try to add something in the buffer
        if self.head == -1:
            self.head = 0

        # Overwrite the empty / filled slot
        self.items[self.tail] = item 

        # Increase the counter. In case that the counter reached it's capacity, we know that the tail will be set to overwrite the items, so, that doesn't mean that we will have more items in the list, it will just overwrite them, therefore, in the case the self.counter property will remain self.capacity, so normally we would have to choose between min([self.capacity, self.counter + 1])
        self.counter = min([self.capacity, self.counter + 1])

        # We are sure that we overwrote / filled an empty slot. Hence it is impossible for the circular buffer to be empty, therefore we wil set the self.IS_EMPTY_FLAG property to False 
        self.IS_EMPTY_FLAG = False

    def dequeue(self):
        # In case that the buffer is empty, raise an exception
        if self.is_empty():
            raise Exception("The buffer is empty. It can't dequeue any item.")

        # Delete ( set the slot to 'None', as None represents in the buffer an empty slot ) the slot
        self.items[self.head] = None

        # Decrement the counter & increase the head value
        self.counter -= 1
        self.head += 1
        
        # We incremented the counter, it could now be bigger than the capacity and if we don't reset it back to 0, next time when we will try to dequeue something from the list, python will give us an error. Hence we will set it to 0.
        if self.head == self.capacity:
            self.head = 0

        # In case that the counter is 0, set the self.IS_EMPTY_FLAG property to True  
        if self.counter == 0:
            self.IS_EMPTY_FLAG = True
            # In case that the user chose to reset the buffer after a full deletion, reset the buffer using the self.resetBuffer() method.
            if self.resetAfter_FullDeletion:
                self.resetBuffer() 
