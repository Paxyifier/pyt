class CircularQueue:
    def __init__(self,len):
        self.items = [None]*len
        self.front = 0
        self.count = 0
    def enqueue(self,item):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))
        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1
    def dequeue(self):
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x
    def resize(self,length):
        ol = self.items
        self.items = [None]*length
        i = self.front
        for j in range(self.count):
            self.items[j] = ol[i]
            i = (i+1)%len(ol)
        self.front = 0
        print("List full Hence resized to Double")
    def isEmpty(self):
        return self.count==0
    def display(self):
        if not self.isEmpty():
            return (self.items[self.front : self.front+(self.count%len(self.items))])  #
    def count(self):
        return self.count
    def peek(self):
        return(self.items[self.front])
if __name__=="__main__":
    x = int(input("Enter the Length of the Circular Queue : "))
    c = CircularQueue(x)
    while True:
        print("What do you want to do: ")
        print("\t1.Enqueue\n\t2.Dequeue\n\t3.Display\n\t4.Peek\n\t5.Size")
        i = int(input("Enter Your Choice : "))
        if i == 0 : break
        elif i == 1 :
            z = input("Enter the element you want to enqueue : ")
            c.enqueue(z)
        elif i == 2 :
            print(c.dequeue())
        elif i == 3 :
            print(" , ".join(map(str,c.display())))
            #c.display()
        elif i == 4 :
            print(c.peek())
        elif i == 5 :
            print(c.size())