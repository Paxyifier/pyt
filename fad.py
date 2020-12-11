def mergesort(a,b):
    temp=[]
    i=0
    j=0
    k=0
    n1 = len(a)
    n2 = len(b)
    while i <= n1 - 1 and j <= n2-1 :
        if a[i]<b[j]:
            temp.append(a[i])
            i+=1
        else:
            temp.append(b[j])
            j+=1
        k+=1
    if i>=n1-1:
        for j in range (j+1,len(b)):
            temp.append(b[j])
    if j>=n2-1:
        for i in range(i+1,len(a)):
            temp.append(a[i])
    print(temp)
    print(temp)
x =[9,11,15,31,39,43]
y =[2,10,17,29,40,45,67,79]
mergesort(x,y)
print()