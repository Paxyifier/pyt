# def sort(a):
# 	n = len(a)
# 	temp = [None]*n
# 	sort(a,temp,0,n-1)
def mergesort(a):
	if len(a) > 1:
		mid = len(a)//2 -1
		L = a[mid:]
		R = a[:mid]
		mergesort(L)
		mergesort(R)
	i = j = k = 0

	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			a[k] = L[i]
			i += 1
		else :
			a[k] = R[j]
			j += 1
		k += 1
	while i < len(L):
		a[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		a[k] = R[j]
		j += 1
		k += 1
z = [9,8,7,6,5,4,3,2,1,0]
mergesort(z)