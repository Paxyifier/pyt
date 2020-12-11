def insertion_sort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j=i-1
        while j >= 0 and a[j] > temp :
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
    print(a)
def sel_sort(a):
    for i in range(len(a)-1):
        minindex = i
        for j in range( i + 1 , len(a)):
            if a[j] < a [minindex]:
                minindex = j
        if i != minindex :
            a[i] , a[minindex] = a[minindex] , a[i]
    print(a)
x = [9,8,7,6,5,4,3,2,1]
def bubble_sort(a):
    n = len(a) 
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1] : 
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag :
            break
    print(a)
def shell_sort(a):
    pass
def mergesort(a,b):
    temp=[]
    i=0
    j=0
    k=0
    n1 = len(a)
    n2 = len(b)
    while i <= n1 - 1 and j <= n2-1 :
        try:
            if a[i]<b[j]:
                temp.append(a[i])
                i+=1
            else:
                temp.append(b[j])
                j+=1
            k+=1
        except:
            print(i,j,a,b,temp,sep="\n")
            break
    if i>=len(a)-1:
        for j in range (j+1,len(b)):
            temp.append(b[j])
    if j>=len(b)-1:
        for i in range(i+1,len(a)):
            temp.append(a[i])
        
    return temp


insertion_sort(x.copy())
sel_sort(x.copy())
bubble_sort(x.copy())
y =[9,11,15,31,39,43]
z =[2,10,17,29,40,45,67,79]
merged = mergesort(x,y)
print(merged)
