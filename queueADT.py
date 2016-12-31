class QueueADT:
    def __init__(self):
        self.container = []
        self.the_queue = []
        #self.visited = [starting_node]

    def push(self, value):             # First item is at front of the list/index 0
        self.container.append(value)
    def pop(self):
        return self.container.pop(0)   # How would this work with an empty list?
    def is_empty(self):
        if self.container == []:
            return True
        else:
            return False
