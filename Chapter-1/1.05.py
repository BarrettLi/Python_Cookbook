# Problem: You want to implement a queue that sorts items by a given priority and always returns
# the item with the highese priority on each pop operation.

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # insert a turple to the list _queue
        # the heappop only pops the "smallest" element from the list, so negate the priority makes 
        # it to pop the correct order
        # the index makes it to pop the correct order as the element was inserted
        heapq.heappush(self._queue, (-priority, index, item))
        self._index += 1

    def pop(self):
        # heappop returns the tuple
        # [-1] of the tuple is the item
        heapq.heappop(self._queue)[-1]


# example of how it might be used:
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1) 
q.pop()
q.pop()
q.pop()
q.pop()
