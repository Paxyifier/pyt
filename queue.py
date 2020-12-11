class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
    def isEmpty(self):
        return self.front==len(self.items)
    def size(self):
        return len(self.items)-self.front
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        try :
            x = self.items[self.front]
            print(x)
            self.items[self.front]=None
            self.front +=1
            return x
        except :
            return "Queue is empty."
    
    def peek(self):
        return self.items[self.front]
    def display(self):
        return self.items[self.front:]
if __name__=="__main__":
    c = Queue()
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
        elif i == 4 :
            print(c.peek())
        elif i == 5 :
            print(c.size())