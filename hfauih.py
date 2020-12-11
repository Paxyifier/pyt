def insertion_sort(a):
	for i in range(1,len(a)) :
		temp = a[i]
		j=i-1
		while j >=0 and a[j] > temp :
			a[j+1] = a[j]
			j-=1
		a[j+1]= temp
x=[9,8,7,6,5,4,3,2,1,0]
insertion_sort(x)
print(x)