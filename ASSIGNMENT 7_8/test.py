class queue:
    def __init__(self):
        self.queue=[] #list

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        #if the list is not empty, then use pop
        if not self.queue.isempty():
            removed=self.queue.pop(0)
            print("The removed element is {removed}")

    def isempty(self):
        return len(self.queue) == 0 
    
    def display(self):
        print("The queue is : {self.queue}")

q=queue()
q.enqueue(1)
q.enqueue(40)
q.display()