'''2. Write a Python program to create a class representing a queue data structure. Include methods
for enqueueing and dequeuing elements.'''
class queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.isempty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty!")
            return None

    def isempty(self):
        return len(self.queue) == 0

    def display(self):
        if self.isempty():
            print("Queue is empty!")
        else:
            print("Queue = ", " ".join(map(str, self.queue)))

a = int(input("Enter How Many Queue You want = \n"))
o = queue()

for i in range(a):
    c = int(input("Enter Data = \n"))
    o.enqueue(c)

print("\nDisplay...\n\n")
o.display()

d = int(input("\n\nEnter How many times you wanna dequeue = \n"))

for i in range(d):
    o.dequeue()

print("\nDisplay...\n\n")
o.display()