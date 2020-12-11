class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class QueueUsingLL:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self): return bool(not self.front)
    def enqueue(self,data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.rear = temp
        self.rear.next = temp
        self.rear = temp
        return
    def dequeue(self):
        if self.isEmpty(): return "Empty List"
        x = self.front.data
        self.front = self.front.next
        return x
    def peek(self):
        return self.front.data
    def size(self):
        p = self.front
        i = 0
        while p is not None:
            i += 1
            p = p.next
        return i
    def display(self):
        if self.front is None:return 'Empty list'
        else:
            p = self.front
            llstr = []
            while p is not None:
                llstr.append(p.data)
                p = p.next
            return llstr
if __name__=="__main__":
    c = QueueUsingLL()
    while True:
        print("What do you want to do: ")
        print("\t1.Enqueue\n\t2.Dequeue\n\t3.Display\n\t4.Peek\n\t5.Size")
        i = int(input("Enter Your Choice : "))
        if i == 0 : break
        elif i == 1 :
            z = input("Enter the element you want to enqueue : ")
            c.enqueue(z)
        elif i == 2 :print(c.dequeue())
        elif i == 3 :print(" , ".join(map(str,c.display())))
        elif i == 4 :print(c.peek())
        elif i == 5 :print(c.size())